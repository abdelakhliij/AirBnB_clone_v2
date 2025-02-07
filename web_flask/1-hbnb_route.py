#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """a function that print hello hbnb! at the root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """a function that print hbnb! at the root"""
    return "HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
