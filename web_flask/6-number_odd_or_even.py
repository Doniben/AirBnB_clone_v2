#!/usr/bin/python3
""" Script that starts a Flask web application with /, /hbnb, /c/<text>,
/python/<text>, /number/<n>, /number_template/<n>, /number_odd_or_even/<n> """

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def route():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def changed_text(text):
    return "C " + text.replace("_", " ")

@app.route('/python/')
@app.route('/python/<text>')
def py_function(text="in cool"):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number_function(n):
    return "%d is a number" % n

@app.route('/number_template/<int:n>')
def template_function(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
