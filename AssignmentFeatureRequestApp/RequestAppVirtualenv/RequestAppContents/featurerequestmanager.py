#Importing flask object
from RequestAppContents import object_flask
#Importing  request, jsonify from flask 
from flask import  request, jsonify
#Importing FeatureRequestTable class from model
from RequestAppContents.model import FeatureRequestModel
#Importing CreateRetreiveService class from featurerequestservice
from RequestAppContents.featurerequestservice import CreateRetreiveService

# FeatureRequestManger class acts as simple webservice layer used for receive Form Requests and getTableDetails
class FeatureRequestManager:
    #Route '/createFeature' is used to recieve POST request from formrequest.html    
    try:
        @object_flask.route('/createFeature', methods=['POST'])
        #receiveFormRequest() is used to recieve feature details from form page in json and submit them to service layer
        def receiveFormRequest():
            #creating instance of CreateRetreiveService class 
            objectService= CreateRetreiveService()
            #receiving values that are entered in the form and sending form values to service layer
            objectService.createFeatureRequest(FeatureRequestModel(request.json['title'], request.json['description'], request.json['client'],request.json['clientPriority'],request.json['targetDate'],request.json['productArea']))
            #Returns a string resoponse if values are persisted in database successfully
            return "successfully inserted data into database"
    # Surrounding with try & except to catch exception if raised any 
    except Exception as e:
        print("Error Occured in receiveRequest",e)


    try:
        #Route '/getdata' is used to send database values whenever a get reqeust happens    
        @object_flask.route('/getdata', methods=['GET'])
        def getTableDetails():
            #creating instance of CreateRetreiveService class 
            objectRequest= CreateRetreiveService()
            #Getting database values from service layer to web service layer
            eachRow= objectRequest.retreiveFeatureRequest()
            #returning values into JSON format
            return jsonify({'rowValues': eachRow})
    # Surrounding with try & except to catch exception if raised any 
    except Exception as e:
        print("Error Occured in getRequest",e)