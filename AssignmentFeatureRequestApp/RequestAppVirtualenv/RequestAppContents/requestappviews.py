#Importing flask object
from RequestAppContents import object_flask
#Importing rendertemplate from flask package
from flask import render_template
#creating route for form.html
@object_flask.route('/')
def form():
    return render_template('formrequest.html')
#creating route for table.html   
@object_flask.route('/table', methods=['GET'])
def table():
    return render_template('tablerequest.html')

