
from flask_sqlalchemy import SQLAlchemy # Importing SQLAlchemy from flask_sqlalchemy package 
from RequestAppContents import object_flask #importing flask object
from RequestAppContents.config import Config
#Config.db.Model is baseclass of all models present in sqlalchemy instance we are inheriting
class FeatureRequestTable(Config.db.Model):
    #creating table name
    __tablename__='FeatureRequestTable'
#creating table columns using Config.db object
    title = Config.db.Column(Config.db.String(100), primary_key=True)
    description = Config.db.Column(Config.db.String(200))
    client = Config.db.Column(Config.db.String(50))  
    clientPriority = Config.db.Column(Config.db.Integer)
    targetDate = Config.db.Column(Config.db.Date())
    productArea = Config.db.Column(Config.db.String(20))
    
    def __init__(self, title, description, client, clientPriority, targetDate, productArea):
        self.title= title
        self.description = description
        self.client = client
        self.clientPriority = clientPriority
        self.targetDate = targetDate
        self.productArea = productArea

