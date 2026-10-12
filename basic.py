# import the Flask class
from flask import Flask

# create an instance of Flask with this file's name
app = Flask(__name__)


# define the function for the home page
@app.route("/")
def home():
    return "<h1>Fitness Tracker Prototype</h1>"


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
