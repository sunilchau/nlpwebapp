from flask import Flask, render_template, request
from db import Database
app = Flask(__name__)
dbo = Database()
@app.route("/")
def index():
    # return "<h1 style = 'color:green'> Happy New Year 2023</h1>"
    return render_template('login.html')


@app.route("/register")
def registration():
    return render_template('register.html')


@app.route("/perform_registration", methods=['post'])
def performregistration():
    name = request.form.get("user_ka_name")
    #print(name)
    email = request.form.get("user_ka_email")
    #print(email)
    password = request.form.get("user_ka_password")
    #print(email)
    response = dbo.insert(name, email, password)
    if response:
        return "Registration successful"
    else:
        return "Email already exists"


app.run(debug=True)
