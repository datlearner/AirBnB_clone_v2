#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
