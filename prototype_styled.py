"""
BASIC PROTOTYPE WITH STYLING

"""

# import the Flask class
from flask import Flask, render_template

# create an instance of Flask with this file's name
app = Flask(__name__)


# define the function for the home / index page
@app.route("/")
def home():
    return render_template("index.html")


# define the function for the login page
@app.route("/login")
def login():
    return render_template("login.html")


# define the function for the steps page
@app.route("/steps")
def steps():
    return render_template("steps.html")


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
