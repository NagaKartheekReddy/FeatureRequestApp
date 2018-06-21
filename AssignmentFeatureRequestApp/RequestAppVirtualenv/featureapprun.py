#Importing flask object
from RequestAppContents import object_flask
#Importing Config class
from RequestAppContents.config import Config

#Creating table using SQLAlchemy object db from Config class
Config.db.create_all()