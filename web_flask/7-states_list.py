#!/usr/bin/python3
"""Starts a flask web app
listenss on 0.0.0.0, port 5000

Routes:
/states_list: display a HTML page: (inside the tag BODY)

"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
Display html page with a list of all state obj in dbstorage
states are sorted by name.
    """
    states = storage.all("state")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """end sqlakchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
