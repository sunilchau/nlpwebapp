from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Happy New Year 2023"

app.run(debug = True)