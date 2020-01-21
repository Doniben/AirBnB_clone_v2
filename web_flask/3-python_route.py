#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask("__main__")


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def change_underscore(text):
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def py_func(text="is cool"):
    return "Python " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
