# Importing SQLAlchemy from flask_sqlalchemy package 
from flask_sqlalchemy import SQLAlchemy 
#importing flask object
from RequestAppContents import object_flask 


# Config class is used for configuring database for connection string and tablename
class Config:
    #SQLALCHEMY_DATABASE_URI it is a configuration variable which gives location of the application's database to Flask-SQLAlchemy
    object_flask.config['SQLALCHEMY_DATABASE_URI']='mysql://root:Password0$@localhost:3306/requestdatabase'
    #instantiating db object using sqlalchmey passing flask object now we can use this sqlalchmey object in flask project
    db = SQLAlchemy(object_flask)
    #initializing a table variable for setting table name in model.py
    tableName='FeatureRequestTable'