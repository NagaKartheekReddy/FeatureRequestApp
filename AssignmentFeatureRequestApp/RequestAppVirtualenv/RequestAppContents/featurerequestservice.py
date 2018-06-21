#importing Config class which has SQLAlchemy connections
from RequestAppContents.config import Config
#importing FeatureRequestTable class from model
from RequestAppContents.model import FeatureRequestModel
#importing sqlalchemy exceptions
from sqlalchemy.exc import * 


#CreateRetreiveService is used to create, retrieve and reprioritize the feature requests from/to database
class CreateRetreiveService:

    # __init__ is default constructor used to declare a class level session variable which can be set or get whenever required for a session
    def __init__(self):
        self.session= ''

    # setSession function is used to set session variable for example to set mock sessions
    def setSession(self, argSession):
        self.session= argSession

    # getSession function is used to get session which is used to create and retrieve values
    def getSession(self):
        if self.session == '': 
            self.session= Config.db.session
            return self.session            
        else:            
            return self.session

    #createFeatureRequest funciton is used to recieve form values from sevice layer and param 'formValues' and create or reprioritize the features       
    def createFeatureRequest(self,formValues):

        try:        
            #Get the client priority for reprioritize of feature request
            clientPriorityReprioritize = int(formValues.clientPriority)
            #Get the length of total rows from feature request accoriding to client given
            totalFeaturesClient=len(self.getSession().query(FeatureRequestModel).filter_by(client=formValues.client).all())
            #Get the client type
            clientType=formValues.client
            #If given client priotity is less than the existing total number of rows
            if clientPriorityReprioritize <= totalFeaturesClient:
                #Calling reprioritize function                
                self.reprioritizeRequest(clientPriorityReprioritize,totalFeaturesClient,clientType)
                self.getSession().add(formValues)
            else:
                #If total number of rows are less than the given priority then it must be in sequence with the existing rows
                self.getSession().add(FeatureRequestModel(formValues.title,formValues.description,formValues.client,totalFeaturesClient+1,formValues.targetDate,formValues.productArea))
            self.getSession().commit() 
        # Surrounded with try except for programming error    
        except ProgrammingError as pe:
            self.getSession().rollback()
            print("Error Occured due some programming issues",pe)
            return "error"
        # Surrounded with try except for any exception    
        except Exception as e:
            self.getSession().rollback()
            print("Error Occured in createFeatureRequest",e)
            return 'Error Occured' 
        # Finally closes the session
        finally:
            self.getSession().close() 
    # reprioritizeRequest  function for reprioritzing the features 
    def reprioritizeRequest(self,clientPriorityReprioritize,totalFeaturesClient,clientType):
        try:
            # For loop is used to reprioritize the requests present in the table
            for clientPriorityReprioritize in range(clientPriorityReprioritize, totalFeaturesClient+1,1):
                (self.getSession().query(FeatureRequestModel).filter_by(clientPriority=clientPriorityReprioritize, client = clientType).first()).clientPriority+=1
        # Surrounded with try except for any exception 
        except Exception as e:
            self.getSession().rollback()
            print("Error Occured in reprioritizeRequest",e)
            return 'Error Occured'
        # Finally closes the session
        finally:
            self.getSession().close()

    #retreiveFeatureRequest function is used to retrieve values from database        
    def retreiveFeatureRequest(self):
        try:
            #retrieves all rows from database
            rowValues=FeatureRequestModel.query.all()
            #creating a empty list
            totalRows = []
            #Iterating the row values according to columns
            for rowValue in rowValues:
                #creating empty dictionary
                splitValues ={}
                #Inserting values into dictionary 
                splitValues['title']=rowValue.title
                splitValues['description']=rowValue.description
                splitValues['client']=rowValue.client
                splitValues['clientPriority']=rowValue.clientPriority
                splitValues['targetDate']=rowValue.targetDate
                splitValues['productArea']=rowValue.productArea
                #Appending the values of dictionary into lists
                totalRows.append(splitValues)
            return totalRows
        # Surrounded with try except for any exception                 
        except Exception as e:
            print("Error Occured in retrieveFeatureRequest",e)
            return 'Error Occured'