# import the Flask class
from flask import Flask

# create an instance of Flask with this file's name
app = Flask(__name__)


# define the function for the index page
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


# define a second function to request your name for a proper greeting
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"


# define a function which doubles a number
@app.route("/double/<num>")
def double(num):
    return f"2 × {num} = {int(num) * 2}"


# define a function which adds two numbers
@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    return f"{num1} + {num2} = {int(num1) + int(num2)}"


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
