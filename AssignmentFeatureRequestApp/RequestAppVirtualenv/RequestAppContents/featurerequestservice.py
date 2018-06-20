#importing Config class which has SQLAlchemy connections
from RequestAppContents.config import Config
#importing FeatureRequestTable class from model
from RequestAppContents.model import FeatureRequestTable
from sqlalchemy.exc import * #importing sqlalchemy exceptions



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
    def createFeatureRequest(self,formValues):
        try:        
        #checking for any features present in database
            clientPriorityReprioritize = int(formValues.clientPriority)
            totalFeaturesClient=len(self.getSession().query(FeatureRequestTable).filter_by(client=formValues.client).all())
            clientType=formValues.client
            if clientPriorityReprioritize <= totalFeaturesClient:                
                self.reprioritizeRequest(clientPriorityReprioritize,totalFeaturesClient,clientType)
                self.getSession().add(formValues)
            else:
                #assumption1:If total number of rows are less than the given priority then it must be in sequence with the existing rows
                self.getSession().add(FeatureRequestTable(formValues.title,formValues.description,formValues.client,totalFeaturesClient+1,formValues.targetDate,formValues.productArea))
            self.getSession().commit() 
        except ProgrammingError as pe:
            self.getSession().rollback()
            print("Error Occured due some programming issues",pe)
            return "error"
        except Exception as e:
            self.getSession().rollback()
            print("Error Occured in createFeatureRequest",e)
            return 'Error Occured' 
        finally:
            self.getSession().close()  
    def reprioritizeRequest(self,clientPriorityReprioritize,totalFeaturesClient,clientType):
        try:
            #assumptiom2:If total number of rows are less than given priority then repriotize of rows should be done
            for clientPriorityReprioritize in range(clientPriorityReprioritize, totalFeaturesClient+1,1):
                (self.getSession().query(FeatureRequestTable).filter_by(clientPriority=clientPriorityReprioritize, client = clientType).first()).clientPriority+=1
        except Exception as e:
            self.getSession().rollback()
            print("Error Occured in reprioritizeRequest",e)
            return 'Error Occured'
        finally:
            self.getSession().close()
    def retreiveFeatureRequest(self):
        try:
            rowValues=FeatureRequestTable.query.all()
            #creating a empty list
            eachRow = []
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
                eachRow.append(splitValues)
            return eachRow
        except Exception as e:
            print("Error Occured in retrieveFeatureRequest",e)
            return 'Error Occured'