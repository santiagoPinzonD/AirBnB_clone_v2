#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask
from flask import request
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
def variables(text):
    """this function print parameters of the URL"""
    new_string = text.replace("_", " ")
    return 'C {}'.format(new_string)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
