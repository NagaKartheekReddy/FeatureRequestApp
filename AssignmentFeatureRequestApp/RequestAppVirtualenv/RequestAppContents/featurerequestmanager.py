#Importing flask object
from RequestAppContents import object_flask
#Importing  request from flask 
from flask import  request, jsonify
#Importing FeatureRequestTable class from model
from RequestAppContents.model import FeatureRequestTable
#Importing CreateRetreiveService class from featurerequestservice
from RequestAppContents.featurerequestservice import CreateRetreiveService
try:
    @object_flask.route('/createFeature', methods=['POST'])
    def receiveRequest():
        #Title=request.json['title']
        #creating instance of CreateRetreiveService class 
        objectService= CreateRetreiveService()
        #receiving values that are entered in the form
        formValues= FeatureRequestTable(request.json['title'], request.json['description'], request.json['client'],request.json['clientPriority'],request.json['targetDate'],request.json['productArea'])
        #sending form values to service layer
        objectService.createFeatureRequest(formValues)
        return "successfully inserted data into database"
except Exception as e:
    print("Error Occured in receiveRequest",e)
try:
    @object_flask.route('/getdata', methods=['GET'])
    def getRequest():
        #creating instance of CreateRetreiveService class 
        objectRequest= CreateRetreiveService()
        #Getting database values from service layer to web service layer
        eachRow= objectRequest.retreiveFeatureRequest()
        #returning values into JSON format
        return jsonify({'rowValues': eachRow})
except Exception as e:
    print("Error Occured in getRequest",e)