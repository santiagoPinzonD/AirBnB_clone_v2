#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """this function return a mss of hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def world():
    """this function return other mss"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def displaytext(text):
    """this function print parameters of the URL"""
    new_string = text.replace("_", " ")
    return 'C {}'.format(new_string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displayPython(text="is cool"):
    """this function print parameters of the URL
        with default value of text"""
    new_string = text.replace("_", " ")
    return 'Python {}'.format(new_string)


@app.route('/number/<int:n>', strict_slashes=False)
def displayonlyisinteger(n):
    """this function print parameters of the URL
        only if is integer"""
    return '{} is a number' .format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """this function render a file of the URL
        only if is integer a parameter passed"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """this function render a file of the URL
        only if is integer a parameter passed"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
