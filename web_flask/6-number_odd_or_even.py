#!/usr/bin/python3
""" Script that starts a Flask web application with /, /hbnb, /c/<text>,
/python/<text>, /number/<n>, /number_template/<n>, /number_odd_or_even/<n> """

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """ home route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def changed_text(text):
    """ changed text """
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_function(text="in cool"):
    """ python function """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_function(n):
    """ number function """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_function(n):
    """ template funtion """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ odd or even function """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
