from flask import Flask, render_template, request

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
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        gender=request.form['gender']
        color=request.form['color']
        return f"Hello {name}"
    else:
        return render_template('form.html')
    
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        gender=request.form['gender']
        color=request.form['color']
        return f"Hello {name}"

if __name__=="__main__":
    app.run(debug=True)