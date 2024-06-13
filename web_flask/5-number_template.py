#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function that returns Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that returns HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """function that returns C followed by the value of the text variable"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """function that returns Python followed by the value of the text
    variable"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function that returns n is a number if n is an integer"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    """Starts a Flask web application"""
    app.run(host='0.0.0.0', port=5000)
