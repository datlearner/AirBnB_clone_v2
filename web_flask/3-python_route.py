#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask, url_for, redirect


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
def python():
    """ python route configuration """

    return redirect(url_for("python_text", text="is_cool"))


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """ python route configuration """

    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
