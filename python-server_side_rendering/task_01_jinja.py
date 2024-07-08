#!/usr/bin/python3
""" Set up a Flask environment and create a basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """ renders a HTML template """
    return render_template("index.html")

@app.route("/about")
def about():
    """ renders a HTML template """
    return render_template("about.html")

@app.route("/contact")
def contact():
    """ renders a HTML template """
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)