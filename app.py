from flask import Flask, render_template, request,redirect
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
    # print(name)
    email = request.form.get("user_ka_email")
    # print(email)
    password = request.form.get("user_ka_password")
    # print(email)
    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message="Email Already exists")


@app.route("/perform_login", methods=['post'])
def perform_login():
    email = request.form.get("user_ka_email")
    password = request.form.get("user_ka_password")

    response = dbo.search(email, password)
    if response:
        return redirect("/profile")
    else:
        return render_template('login.html', message="incorrect email/password")


@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/ner")
def ner():
    return render_template('ner.html')

@app.route("/perform_ner", methods =['post'])
def perform_ner():
    return "Yeha NER Hoga"

app.run(debug=True)
