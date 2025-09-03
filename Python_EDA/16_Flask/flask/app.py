<<<<<<< HEAD
from flask import Flask

'''
It Creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask Course. This should be an amazing course."

@app.route("/index")
def index():
    return "Welcome to the index page."



if __name__  == "__main__":
=======
from flask import Flask

'''
It Creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask Course. This should be an amazing course."

@app.route("/index")
def index():
    return "Welcome to the index page."



if __name__  == "__main__":
>>>>>>> 2146a209 (Local)
    app.run(debug=True)