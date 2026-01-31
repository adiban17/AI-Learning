# jinja 2 template engine
'''
{{ }}: expressions to print output in html
{%.....%}: conditionals, for loops
{#....#}: single line comments
'''
from flask import Flask, render_template, request

app=Flask(__name__) # creating a WSGI server

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

 # Variable Rule   
@app.route('/success/<int:score>')
def success(score):
    if score>40:
        res="passed"
    else:
        res="failed"
    return render_template("result.html",result=res)

@app.route('/success_res/<int:score>')
def success_res(score):
    if score>40:
        res="passed"
    else:
        res="failed"

    exp={"Score":score,"Result":res}

    return render_template("result1.html",result=exp)

if __name__=="__main__":
    app.run(debug=True)