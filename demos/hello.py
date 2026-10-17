# import the Flask class and the template renderer
from flask import Flask, render_template

# create an instance of Flask with this file's name
app = Flask(__name__)


# define the function for the index page
@app.route("/")
def index():
    return "Hello, World!"


# define a greeting function
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
