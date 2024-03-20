#!/usr/bin/python3
""" This script creates a flash application """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ removes the current session """

    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ returns all the states in DBstorage """

    states = storage.all("State")
    states_arr = [
            {"id": state.id, "name": state.name}
            for state in states.values()
    ]
    states_arr = sorted(states_arr, key=lambda x: x["name"])

    return render_template("7-states_list.html", states=states_arr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
