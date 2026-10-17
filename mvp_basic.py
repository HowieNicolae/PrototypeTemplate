"""
BASIC MVP (MINIMUM VIABLE PRODUCT)

"""

# import the Flask class
from flask import Flask, request, jsonify, render_template

# create an instance of Flask with this file's name
app = Flask(__name__)


# Proof-of-concept mock implementation.
# Production MVP deployment requires a robust database solution like SQLite.
CREDENTIALS = (
    {"username": "admin", "password": "secr3t"},
    {"username": "Bob", "password": "pie67"},
    {"username": "Mary", "password": "abc123"},
)

STEPS_DATA = {"current": 6000, "goal": 10000}


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

    # return JSON error message
    return jsonify({"error": "Invalid credentials"}), 401


# define the function for the steps page
@app.route("/steps")
def steps():
    # pass the metrics dict to the template as a variable named 'data'
    return render_template("steps_mvp.html", data=STEPS_DATA)


@app.route("/steps/add/<count>")
def add(count):
    try:
        # convert the count variable to an integer and update current steps
        STEPS_DATA["current"] += int(count)

        # return a JSON success message instead of rendering the full page
        return (
            jsonify(
                {
                    "message": "Steps updated successfully",
                    "new_total": STEPS_DATA["current"],
                }
            ),
            200,
        )

    except Exception as e:
        # return JSON error message
        return jsonify({"error": str(e)}), 400


# standard coding partice for when running a python file from the command line
if __name__ == "__main__":
    app.run(debug=True)
