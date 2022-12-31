from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   #return "<h1 style = 'color:green'> Happy New Year 2023</h1>"
    return render_template('login.html')

app.run(debug = True)