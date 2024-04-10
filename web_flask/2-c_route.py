#!bin/usr/python3
""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hello_c():
    return "C  

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0", port=5000)