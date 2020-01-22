#!/usr/bin/python3
""" Python script that starts a Flask web application with /,
/hbnb, /c/<text>, /python/<text>, /number/<n>/ and /number_template/<n> """

from flask import Flask
from flask import render_template

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
def python_route(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    return ("%d is a number" % n)


app.route('number_template/<int:n>')
def template(n):
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
