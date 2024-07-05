#!/usr/bin/python3
""" Set up a Flask environment and create a basic Flask app"""

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """ renders a HTML template """
    return render_template("index.html")

@app.route("/items")
def items():
    """ renders a HTML template """

    items_list = []

    with open("./data/items.json", 'r') as f:
        rows = json.load(f)
    for key,value in rows.items():

        items_list = value

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)