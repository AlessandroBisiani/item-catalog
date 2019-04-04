#! /usr/bin/env python3
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.types import VARCHAR, BLOB
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# sqlalchemy entry point
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    email = Column(VARCHAR(350), primary_key=True)
    name = Column(String(250), nullable=False)

class Category(Base):
    __tablename__ = 'categories'

    name = Column(String(100), primary_key=True)

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    category = Column(Integer, ForeignKey('categories.name'))
    owner = Column(String(250), ForeignKey('users.email'))
    title = Column(String(100), nullable=False)
    body = Column(BLOB())

    category = relationship(Category)#back_populates='notes')
    user = relationship(User)#back_populates='notes')

# create a database in notes.db and return a connection to it
engine = create_engine('sqlite:///notes.db')
# Instantiate the classes herein as tables.
Base.metadata.create_all(engine)
