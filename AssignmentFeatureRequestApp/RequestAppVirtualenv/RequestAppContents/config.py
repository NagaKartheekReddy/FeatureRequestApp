from flask_sqlalchemy import SQLAlchemy # Importing SQLAlchemy from flask_sqlalchemy package 
from RequestAppContents import object_flask #importing flask object

class Config:
    #SQLALCHEMY_DATABASE_URI it is a configuration variable which gives location of the application's database to Flask-SQLAlchemy
    object_flask.config['SQLALCHEMY_DATABASE_URI']='mysql://root:Password0$@localhost:3306/requestdatabase'
#instantiating db object using sqlalchmey passing flask object now we can use this sqlalchmey object in flask
    object_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    db = SQLAlchemy(object_flask)