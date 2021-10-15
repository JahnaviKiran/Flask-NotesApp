from enum import unique
from flask_sqlalchemy import SQLAlchemy
from . import db #importing db object from __init__.py
from flask_login import UserMixin #custom class to give specifics for user login
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #associating Note with the User
    # one-to-many relationship : one-user many-notes
    # user.id in lowercase as columns by default are lowercase
    #id is the primary key

class User(db.Model, UserMixin):  #User inherits from the two
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship ('Note') #since its a relationship, it remains uppercase

# def __init__(self, id, email, password, first_name):
 
#         self.id = id
#         self.email = email
#         self.password = password
#         self.first_name = first_name

