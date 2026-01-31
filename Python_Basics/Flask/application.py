from flask import Flask

app=Flask(__name__) # creating a WSGI server
'''
It creates an instance of the Flask class,
which will be your WSGI (web-server gateway interface) application.
'''

@app.route('/')
def welcome():
    return("Welcome to This Flask App! This is an amazing app.")

@app.route('/index')
def index():
    return("This is the index page!")

if __name__=="__main__":
    app.run(debug=True)