from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Mike"
    return render_template("index.html", name=name)

@app.route("/french")
def home():
    return "<div><p>Bonjour, World!</p></div>"

@app.route("/name/<name>")
def hello_name(name):
    return f"Hello, {name}"

# Mac
# FLASK_APP=hello.py flask run

# FLASK_APP=hello.py FLASK_DEBUG=true flask run


# Windows?
# $env:FLASK_APP = 'hello.py'; flask run
# $env:FLASK_APP = 'hello.py'; $env:FLASK_ENV = 'development'; flask run