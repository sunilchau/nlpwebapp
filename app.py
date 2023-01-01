from flask import Flask, render_template, request, redirect, session


from db import Database
import api

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

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
        session['logged_in'] = 1
        return redirect("/profile")
    else:
        return render_template('login.html', message="incorrect email/password")


@app.route("/profile")
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route("/ner")
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')


@app.route("/perform_ner", methods=['post'])
def perform_ner():
    if session:
        nertext = request.form.get("ner_text")
        response = api.ner(nertext)
        print(response)
        return render_template('ner.html', response=response)
    else:
        return redirect('/')


app.run(debug=True)
