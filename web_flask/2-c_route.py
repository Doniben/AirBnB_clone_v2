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
def replace_text(text):
    return "C " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
