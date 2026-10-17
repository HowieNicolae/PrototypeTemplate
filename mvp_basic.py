"""
BASIC MVP (MINIMUM VIABLE PRODUCT)

"""

# import the Flask class
from flask import Flask, request, jsonify, render_template

# create an instance of Flask with this file's name
app = Flask(__name__)


# one would not do this for a real-world MVP
# rather use sqlite database to store usernames and passwords
CREDENTIALS = (
    {"username": "admin", "password": "secr3t"},
    {"username": "Bob", "password": "pie67"},
    {"username": "Mary", "password": "abc123"},
)


# define the function for the home / index page
@app.route("/")
def home():
    return render_template("index.html")


# define the function for the login page
@app.route("/login")
def login():
    return render_template("login_mvp.html")


# authenticate login credential
# example usage:
# http://127.0.0.1:5000/login/authenticate?usr=admin&pwd=secret
@app.route("/login/authenticate", methods=["GET"])
def authenticate():
    # Use .get() to grab a single value
    username = request.args.get("usr")
    password = request.args.get("pwd")

    # error checking
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # check credentials here
    for cred in CREDENTIALS:
        if cred["username"] == username and cred["password"] == password:
            return jsonify({"message": "Login successful!"}), 200

    return jsonify({"error": "Invalid credentials"}), 401


# define the function for the steps page
@app.route("/steps")
def steps():
    return render_template("steps.html")


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
