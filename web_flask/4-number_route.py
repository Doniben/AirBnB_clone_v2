#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello HBNB"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def text_function(text):
    return "C" + text.replace("_", " ")

@
