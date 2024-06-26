#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
import os, sys
from models.state import State
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
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
def number_template(n):
    """function that returns n is a number if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """function that returns n is a number if n is an integer"""
    return render_template('6-number_odd_or_even.html', number=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """function that returns HBNB"""
    states = storage.all("State")

    states = sorted(states.values(), key=lambda k: k.name)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""

    storage.close()

if __name__ == "__main__":
    """Starts a Flask web application"""
    app.run(host='0.0.0.0', port=5000)
