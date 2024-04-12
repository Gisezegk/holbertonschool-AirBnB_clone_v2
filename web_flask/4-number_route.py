#!/usr/bin/python3
"script that starts a Flask web application"
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    "starts a Flask web application"
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    "starts a Flask web application"
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    "starts a Flask web application"
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    "starts a Flask web application"
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    "starts a Flask web application"
    return "{} is number".format(n)

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0", port=5000)