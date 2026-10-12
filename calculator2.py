# import the Flask class and request
from flask import Flask, request

# create an instance of Flask with this file's name
app = Flask(__name__)


# define the function for the index page
@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


# define a function which adds multiple numbers
# usage: http://127.0.0.1:5000/add?x=1&x=2&x=3&x=4
@app.route("/add")
def add():
    query = request.args.getlist("x")
    if len(query) > 0:
        nums = [float(x) for x in query]
        return f"<p>Total is {sum(nums)}</p>"
    else:
        return """<p>Please enter a command like this in the address bar:</p>
        http://127.0.0.1:5000/add?x=1&x=2&x=3&x=4"""


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
