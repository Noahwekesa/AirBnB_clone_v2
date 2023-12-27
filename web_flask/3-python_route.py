#!/usr/bin/python3
"""
script that starts a flask web application
"""
from flask import Flask
app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello_flask():
    """
Return Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
Return HBNB on /hbnb route
    """
    return "HBNB"


@app.route('/c/<text>')
def c_cool(text):
    """
Return C followed by the value the text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_cool(text):
    """
    Return the default value of text is "is cool"
    """
    return "python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
