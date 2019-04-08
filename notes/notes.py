#! /usr/bin/env python3.7
from flask import Flask, render_template, request, flash, redirect, url_for, \
        jsonify, make_response

from flask import session as login_session

import httplib2
import random, string, json

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from sqlalchemy.exc import DBAPIError

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from database_setup import Base, Note, Category, User
# import requests

app = Flask(__name__)

''' Create the engine, which is the connection source, then using same
Base (the same orm heirarchy!) as databse_setup, tie the connection supplier
to the base.'''
engine = create_engine('sqlite:///notes.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    # state = hashlib.sha256(os.urandom(1024)).hexdigest()
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    return 'gconnect route'


@app.route('/gdisconnect')
def gdisconnect():
    return 'gdisconnect route'


@app.route('/')
@app.route('/categories/')
def showCategories():
    # return render_template('index.html')
    return 'Index route'


@app.route('/categories/<string:category_name>/')
def showNotes(category_name):
    # return render_template('index.html')
    return 'showNotes() for {}'.format(category_name)


@app.route('/categories/<string:category_name>/notes/<int:id>/')
def showNote(category_name, id):
    # return render_template('index.html')
    return 'showNote() for {} with note id: {}'.format(category_name, id)


@app.route('/categories/<string:category_name>/notes/new/')
def newNote(category_name):
    # return render_template('index.html')
    return 'newNote() in {} category'.format(category_name)


@app.route('/categories/<string:category_name>/notes/<int:id>/edit/',
           methods=['GET', 'POST'])
def editNote(category_name, id):
    # return render_template('index.html')
    return 'editNote() for {} with id: {}'.format(category_name, id)


@app.route('/categories/<string:category_name>/notes/<int:id>/delete/')
def deleteNote(category_name, id):
    # return render_template('index.html')
    return 'deleteNote() for {} with note id: {}'.format(category_name, id)


if __name__ == '__main__':
    app.secret_key = 'liseubpeu4no;3a4nga80[32443ifud5y4tu325zexrctouio78om;8n'
    app.run(host='0.0.0.0', port=5000, debug=True)
