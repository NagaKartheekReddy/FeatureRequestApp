# AssignmentFeatureRequestApp
Built a project 'Feature Request Application' with python, flask, sqlalchemy and knockoutjs.
# Feature Request Application:
	Feature Request App built in Flask which is a web application framework written in Python. 
	It consist of feature request form page where a user can fill in a feature request. The form entry values are binded using KnockoutJS and send as JSON data to webservice layer	using SqlAlchemy ORM details are persisted in database and feature request details page where a user can see feature request list in the form of a table.
  
# Getting Started:
	Pre-requisites: Project is built and validated using the following software
		* Python (v.3.6.5), 
		* MySql database
		* Browsers: Chrome(v.64.) and Firefox(v.55+)
	 
# Installation:
	1.Open GitHub link and download the project folder.
	2.Open command prompt in project folder “AssignmentFeatureRequestApp\RequestAppVirtualenv\Scripts” and type
	‘activate’. This will activate the ‘RequestAppVirtualenv’.

	**.. \AssignmentFeatureRequestApp\RequestAppVirtualenv\Scripts>activate
	**(RequestAppVirtualenv)..\AssignmentFeatureRequestApp\RequestAppVirtualenv\Scripts>
		
	3.Then install required packages present in requirements.txt by executing command ‘pip install –r requirements.txt’ OR
	can run command ‘pip install  package-name’
	**(RequestAppVirtualenv)..AssignmentFeatureRequestApp\RequestAppVirtualenv\Scripts> pip install –r 		    requirements.txt
	4.Set Flask_APP variable by using command ‘set FLASK_APP=featureapprun.py’
	
	**(RequestAppVirtualenv)..AssignmentFeatureRequestApp\RequestAppVirtualenv\Scripts>set FLASK_APP=featureapprun.py
        
	5.Type ‘flask run’ and navigate to ‘http://127.0.0.1:5000/’ you can see Feature Request App form
	
	**(RequestAppVirtualenv)..\AssignmentFeatureRequestApp\RequestAppVirtualenv>flask run
 							* Serving Flask app "featureapprun.py"
							* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# Feature Request Application Form Page:
 	Open chrome/Mozilla and navigate to url ‘http://127.0.0.1:5000/’ where list of fields are present for customer to fill
	in are as follows:
	1.Title: A short, descriptive name of the feature request.
		•Title [String type] Length-100 characters (Will stop user further entering 100 by using html input ‘maxlength’
		 attribute).
		•Title is unique field (Same titles cannot be entered for different clients).
		•Title is Mandatory field (Input validation is done by html attribute ‘required’).
	2.Description: A long description of the feature request.
		•Description [String type] Length- 1000 characters (Will stop user further entering 1000 by using html input 
		‘maxlength’ attribute).
		•Description uses ‘text-area’ html input attribute which can be auto align as required by user.
		•Description filed is not mandatory.
	3.Client: A selection list of clients (use "Client A", "Client B", "Client C")
		•Client [String type] will display list with three options "Client A","Client B", "Client C" (using html  
		‘select’ and ‘options’ type attributes) and user can select any one of the clients.
		•Client field is also mandatory
	4.Client Priority: A numbered priority according to the client (1...n).Client Priority numbers should not repeat for the 
	given client, so if a priority is set on a new feature as "1", then all other feature requests for that client should be 
	reordered.
		•Client Priority [Integer Type]-User can only enter numbers (Will stop user entering String values, by using 
		html input type as ‘number’).
		•Client Priority is mandatory field.
		•User cannot enter any negative values.
		•Client Priority will not be same for two features with respect to a single client as Client Priority will be 
		re-ordered.
	5.Target Date: The date that the client is hoping to have the feature.
		•Target Date [Date type] field displays a calendar (User can select date in the calendar).
		•User can only select future dates and past dates cannot be selected.
		•Target Date is a mandatory field.
	6.Product Area: A selection list of product areas (use 'Policies', 'Billing', 'Claims', 'Reports')
		•Product Area [String Type] field display list of four options 'Policies', 'Billing', 'Claims', 'Reports' (using 
		html ‘select’ and ‘options’ type attributes) and user can select any one of Product Area.
		•Product Area is a mandatory field.    	
# Feature Request Application Details Page:
	Entering all values and on clicking ‘Submit’ it will navigate to details page at url ‘http://127.0.0.1:5000
	/table’ where all the feature request details are reflected in a table [built with jQuery data Table]
	which will have Sorting and Searching
# Application Details:
	The following are requirements on the tech stack. This stack demonstrates mastery of tools our team favors.
	•OS: Windows
	•Server Side Scripting: Python (3.6.5)
	•Server Framework: Flask 
	•SqlAlchemy (1.2.2): Solution Options for Reprioritization
		1.SQL ORM: This has been implemented-ORM tools provide an object oriented query language. This allows application developers to focus on the object model and not to have to be concerned with the database structure or SQL semantics.	The ORM tool itself will translate the query language into the appropriate syntax for the database.
		2.Using Stored Procedure: Stored procedures are compiled once and stored in executable form, so procedure calls are quick and efficient. Executable code is automatically cached and shared among users. This lowers memory requirements and
invocation overhead.

	•JavaScript: KnockoutJS (3.4.2): Knockout is a JavaScript library that which gives a simplified and dynamic Model-View-
	 View Model binding pattern for all the UI elements in HTML.
