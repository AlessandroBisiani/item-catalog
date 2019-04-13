#! /usr/bin/env python3.7
from flask import (
        Flask, render_template, request, flash, redirect, url_for, jsonify,
        make_response
    )
from flask import session as login_session

import httplib2
import random
import string
import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from sqlalchemy.exc import DBAPIError

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from database_setup import Base, Note, Category, User
import requests


app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"

google_client_key = ''
app_secret = ''

with open('keys.txt', 'r') as f:
    keys = f.read()
    for k in keys.split(' '):
        if k.startswith('client_id'):
            google_client_key = k.split('=')[-1]
        elif k.startswith('app_secret'):
            app_secret = k.split('=')[-1]


''' Create the engine, which is the connection source, then using same
Base (the same orm heirarchy!) as databse_setup, tie the connection supplier
to the base.'''
engine = create_engine('sqlite:///notes.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    '''Set the session state, retrieve the current categories, and render
    the login page, passing in the categories and login keys'''
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    # print(f'app state: {state}')
    login_session['state'] = state
    # print(f'login session state is: {login_session["state"]}')
    try:
        categories = session.query(Category).all()
    except Exception as e:
        log_error(e)
    else:
        return render_template('login.html',
                               categories=categories,
                               STATE=state,
                               client_id=google_client_key)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = f'''https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=\
{access_token}'''
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print('Token\'s client ID does not match app\'s.')
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                                 'Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['name'] = data['name']
    login_session['email'] = data['email']

    # See if a user exists, if it doesn't make a new one
    if get_user_id(login_session['email']):
        login_session['id'] = get_user_id(login_session['email'])
    else:
        create_user(login_session)

    output = ''
    output += '<h2>Welcome, '
    output += login_session['name']
    output += '!</h2>'
    name = login_session['name']
    flash(f'Hi, {name} you are now logged in.')
    print('done!')
    return output


# User Helper Functions
def create_user(login_session):
    newUser = User(name=login_session['name'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def get_user_info(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception as e:
        log_error(e)


# DISCONNECT - Revoke a current user's token and reset the login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = f'https://accounts.google.com/o/oauth2/revoke?token={access_token}'
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['name']
        del login_session['email']
        del login_session['id']

        # response = make_response(json.dumps('Successfully disconnected.'), 200)
        # response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('show_categories'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/')
def show_categories():
    user_name = 'User'
    try:
        categories = session.query(Category).all()
        all_notes = session.query(Note).all()
        if 'access_token' in login_session:
            user = session.query(User).filter_by(name=login_session['name']).one()
            user_name = user.name
    except Exception as e:
        log_error(e)
    else:
        '''
        Choose at most 10 notes at random before passing them to the
        index page
        '''
        if len(all_notes) >= 10:
            random_notes = random.sample(all_notes, 10)
        else:
            random_notes = random.sample(all_notes, len(all_notes))
        display_notes = random_notes
    finally:
        return render_template('index.html',
                                categories=categories,
                                notes=display_notes,
                                user_name=user_name)


@app.route('/categories/<string:category_name>')
def show_notes(category_name):
    try:
        category_notes = session.query(Note).filter_by(
                    category_name=category_name).all()
        categories = session.query(Category).all()
    except Exception as e:
        log_error(e)
    else:
        return render_template('categoryNotesView.html',
                               notes=category_notes,
                               categories=categories)


@app.route('/categories/<string:category_name>/notes/<int:id>')
def show_note(category_name, id):
    try:
        display_note = session.query(Note).filter_by(id=id).one()
        categories = session.query(Category).all()
    except Exception as e:
        log_error(e)
    else:
        if display_note.owner_id == login_session['id']:
            return render_template('publicNoteView.html',
                                   note=display_note,
                                   categories=categories)
        else:
            return render_template('noteView.html',
                                   note=display_note,
                                   categories=categories)


@app.route('/categories/<string:category_name>/notes/new',
           methods=['GET', 'POST'])
def new_note(category_name):
    if 'access_token' not in login_session:
        return redirect('/login')
    categories = session.query(Category).all()

    if request.method == 'GET':
        return render_template('newNote.html', categories)
    if request.method == 'POST':
        print('-----------------Reached POST at new_note()-------------------')
        return redirect(url_for('show_categories'))


@app.route('/categories/<string:category_name>/notes/<int:id>/edit',
           methods=['GET', 'POST'])
def edit_note(category_name, id):
    if 'access_token' not in login_session:
        return redirect('/login')
    categories = session.query(Category).all()

    if request.method == 'GET':
        return render_template('editNote.html', categories)
    if request.method == 'POST':
        print('-----------------Reached POST at edit_note()------------------')
        return redirect(url_for('show_categories'))


@app.route('/categories/<string:category_name>/notes/<int:id>/delete',
           methods=['GET', 'POST'])
def delete_note(category_name, id):
    if 'access_token' not in login_session:
        return redirect('/login')
    categories = session.query(Category).all()

    if request.method == 'GET':
        return render_template('deleteNote.html', categories)
    if request.method == 'POST':
        print('-----------------Reached POST at delete_note()----------------')
        return redirect(url_for('show_categories'))


def log_error(error):
    '''Handle error responses that should be logged

    Arguments:
        error {str} -- The exception or error response __repr__
    '''

    # TODO: append to a file
    print(error)


def log_message(response):
    '''Handle non-error responses that should be logged.

    Arguments:
        response {str} -- A description of app functionality that should be 
        logged
    '''
    # TODO: append to a file
    print(response)



if __name__ == '__main__':
    app.secret_key = app_secret
    app.run(host='0.0.0.0', port=5000, debug=True)
