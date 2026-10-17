"""
BASIC PROTOTYPE

"""

# import the Flask class
from flask import Flask

# create an instance of Flask with this file's name
app = Flask(__name__)


# define the function for the home page
@app.route("/")
def home():
    return """
    <h1>Fitness Tracker</h1>

    <a href="/login">Login</a>
    """


# define the function for the login page
@app.route("/login")
def login():
    return """
    <h2>Login Page</h2>

    Username:<br>
    <input><br><br>

    Password:<br>
    <input type='password'><br><br>

    <button>Login</button><br><br>

    <a href="/">Home<a>
    """


# define the function for the steps page
@app.route("/steps")
def steps():
    return """
    <h2>Daily Steps Tracker</h2>

    <p>Today's Steps: 6000</p>
    <p>Goal: 10000</p>

    <button>Add Steps</button><br><br>

    <a href="/">Home<a>
    """


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
