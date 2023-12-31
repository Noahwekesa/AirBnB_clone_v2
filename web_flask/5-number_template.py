#!/usr/bin/python3
"""
script that starts a flask web application
"""
from flask import Flask, render_template
app: Flask = Flask(__name__)
app.strict_slashes = False  # type: ignore


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


@app.route('/number/<n>')
def diplay_number(n):
    """
return n if only n is an integer
    """
    return "{} is a number".format(int(n))


@app.route('/number_template/<n>')
def display_template(n):
    if n.isdigit():
        return render_template('5-number.html', n=int(n))
    else:
        return ""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
