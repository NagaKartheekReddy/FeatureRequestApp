# importing Flask class from flask package
from flask import Flask 
#creating flask object
object_flask=Flask(__name__) 
# importing modules requestappviews, featurerequestmanager, featurerequestservice, model
from RequestAppContents import requestappviews, featurerequestmanager, featurerequestservice, model