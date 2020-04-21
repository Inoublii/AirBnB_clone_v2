#!/usr/bin/python3
# script that starts a Flask web application
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Hello"""
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """text"""
    return("C " + str(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
def display():
    """python display default"""
    return("Python is cool")


@app.route('/python/<text>', strict_slashes=False)
def p_text(text):
    """text"""
    return("Python " + str(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """numbers"""
    return("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """template"""
    return(render_template("5-number.html", num=n))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
