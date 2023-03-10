#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template
from uuid import uuid4

app = Flask(__name__)


@app.route("/3-hbnb", strict_slashes=False)
def cities_by_states():
    """Display an HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("3-hbnb.\
html", states=states, amenities=amenities, places=places, cache_id=(uuid4()))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
