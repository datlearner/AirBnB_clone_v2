#!/usr/bin/python3
""" This script creates an application server for hbnb """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(exception):
    """ removes the current session """

    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ configures the hbnb route """

    states = storage.all("State")
    places = storage.all("Place")
    users = storage.all("User")
    amenities = storage.all("Amenity")

    states_arr = []
    for state in states.values():
        state_dict = {"id": state.id, "name": state.name}
        cities = [{"id": city.id, "name": city.name} for city in state.cities]

        # sort cities
        state_dict["cities"] = sorted(cities, key=lambda x: x["name"])
        states_arr.append(state_dict)

    # sort states
    states_arr = sorted(states_arr, key=lambda x: x["name"])

    users = {
            user.id: "{} {}".format(user.first_name, user.last_name)
            for user in users.values()
    }

    places_arr = [{
        "id": place.id,
        "name": place.name,
        "user": users[place.user_id],
        "description": place.description,
        "rooms": "{} {}".format(
                                place.number_rooms,
                                "room" if place.number_rooms == 1 else "rooms"
                                ),
        "bathrooms": "{} {}".format(
                                    place.number_bathrooms,
                                    "bathroom" if place.number_bathrooms == 1
                                    else "bathrooms"
                                    ),
        "guests": "{} {}".format(
                                place.max_guest,
                                "guest" if place.max_guest == 1 else "guests"
                                ),
        "price": place.price_by_night
    } for place in places.values()]

    # sort places
    places_arr = sorted(places_arr, key=lambda x: x["name"])

    amenities_arr = [amenity.name for amenity in amenities.values()]

    # sort amenities
    amenities_arr.sort()

    return render_template("100-hbnb.html",
                           states=states_arr,
                           places=places_arr,
                           amenities=amenities_arr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
