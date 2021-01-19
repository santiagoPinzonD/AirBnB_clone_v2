#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """this function return a mss of hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def world():
    """this function return other mss"""
    return 'HBNB'

app.run(host='0.0.0.0')
