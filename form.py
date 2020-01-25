'''Creation of Python forms for the department  library/Lab/attendance etc.,  by entering  student  details of each  student . Validate the form using Python validators and display error message

- For this experiment we will use flask framework. It is python web framework used for web development.
- Run the belwo command to install flask.
    # pip install flask
- Create form.html file in the following path templates/form.html
- For validating the from lets use regular expression
- Create response.html in templates folder to see validation erros'''

# import Flask class & render_template from flask module

from flask import Flask, render_template, request, flash, redirect, url_for

# import re for validations

import re

# create application with Flask class

app = Flask(__name__)

# create secret key 

app.secret_key = "form-validation"

# create a function that returns form.html file

@app.route('/')

def attendance():
    return render_template('form.html')

@app.route('/get_data', methods = ['POST', 'GET'])

def get_data():
    r = request.form['no']
    n = request.form['name']
    d = request.form['date']
    a = request.form['att']
    errors = [] # empty list
    #return str((r, n, d, a))
    if(re.match('^[0-9][A-Z0-9]{9}$', r)):
        errors.append("success")
    else:
        errors.append(r+" didn't start with 0-9 or rollno don't have 10 chars")
        
    if(re.match('^[A-Z][a-z]{2, 15}$', n)):
        errors.append("success")
    else:
        errors.append(n+" didn't start with capital letter or it does not having min of 3 chars and max of 15 chars")
    if(re.match('^[0-9][0-9-]{9}$', d)):
        errors.append("success")
    else:
        errors.append(d+" not starting with 0-9 or its length is not 10")
    if(re.match('[PA]{1}$', a)):
        errors.append("success")
    else:
        errors.append(a+" does not contain either P or A")
   
    return render_template("response.html", er = errors, details = [r, n, d, a])
# run the application with host and port number and set debug as True for making changes in application

app.run(debug = True, host = "localhost", port = "8000")