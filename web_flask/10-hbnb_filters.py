#!/usr/bin/python3
""" This script starts a web application for the HBNB project"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ closes the current session """

    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb():
    """ Configures the hbnb filters route """

    states = storage.all("State")
    amenities = storage.all("Amenity")

    states_arr = []
    for state in states.values():
        state_dict = {}
        state_dict["id"] = state.id
        state_dict["name"] = state.name
        cities = [
                {"id": city.id, "name": city.name}
                for city in state.cities
        ]

        # Sort the list by each name key in each dict
        state_dict["cities"] = sorted(cities, key=lambda x: x['name'])
        states_arr.append(state_dict)

    # Sort the states_arr by each name key
    states_arr = sorted(states_arr, key=lambda x: x['name'])

    amenities_arr = [amenity.name for amenity in amenities.values()]
    amenities_arr.sort()

    return render_template("10-hbnb_filters.html",
                           states=states_arr,
                           amenities=amenities_arr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
