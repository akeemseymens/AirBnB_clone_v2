#!/usr/bin/python3

'''Script that starts a Flask web application'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """RETURNS 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return  “C ” and  value text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.rout('/python/<text>', strict_slashes=False)
def python(text='iscool'):
    """Return  “C ” and  value text"""
    return 'Python  %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return /number/n"""
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
