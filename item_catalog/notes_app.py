#! /usr/bin/env python3.7
from flask import Flask, render_template, request, flash, redirect, url_for, \
        jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from sqlalchemy.exc import DBAPIError
from database_setup import Base, Note, Category, User

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
    return 'Login page'


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
    app.run(host='0.0.0.0', port=5000, debug=True)
