#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """this function return a mss"""
    return 'Hello HBNB!'

app.run(host='0.0.0.0')
