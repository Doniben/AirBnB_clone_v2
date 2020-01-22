#!/usr/bin/python3
""" Python script that starts a Flask web application with /,
/hbnb, /c/<text>, /python/<text>, /number/<n>/ and /number_template/<n> """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def Page_hbnb():
    return "HBNB"


@app.route("/c/<text>")
def changed_text(text):
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
