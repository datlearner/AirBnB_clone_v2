#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ home route configuration """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb route configuration """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ c route configuration """

    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    """ python route configuration """

    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ number route configuration """

    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ number template route configuration """

    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ number odd or even route configuration """

    if n % 2 == 0:
        val = "even"
    else:
        val = "odd"

    return render_template("6-number_odd_or_even.html", n=n, val=val)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
