from flask import Flask, render_template

app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello_flask():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_cool(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_cool(text="is_cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>')
def display_number(n):
    return "{} is a number".format(int(n)) if n.isdigit() else ""


@app.route('/number_template/<n>')
def display_number_template(n):
    if n.isdigit():
        return render_template('number_template.html', n=int(n))
    else:
        return ""


@app.route('/number_odd_or_even/<n>')
def display_number_odd_or_even(n):
    if n.isdigit():
        return render_template('6-number_odd_or_even.html', n=int(n), result=is_even_odd(int(n)))
    else:
        return ""


def is_even_odd(num):
    return "even" if num % 2 == 0 else "odd"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
