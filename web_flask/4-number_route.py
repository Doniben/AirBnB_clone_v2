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


@app.route('/python/')
@app.route('/python/<text>')
def python_func(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    return "%d is a number" % n

if __name__ == '__main__':
    app.run(host="0.0.0.0")
