from . import db #databases and stuff
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000)) #the notes lenght
    date = db.Column(db.DateTime(timezone=True), default= func.now()) #stores date and time of user's note
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))# one to many relationship, we figure who created the note by looking at user ID 
    

    
class User(db.Model, UserMixin): #the user primary data
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(150), unique =True)#unique to the user, maximum 150 characters
    password = db.Column(db.String(150)) #same thing but for passwords
    first_name = db.Column(db.String(150))#username
    notes = db.relationship('Note')