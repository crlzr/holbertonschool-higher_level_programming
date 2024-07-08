#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    """ renders a HTML template """
    return render_template('index.html')

@app.route('/items')
def items():
    """ renders a HTML template """
    items_list = []

    with open("./data/items.json", 'r') as f:
        rows = json.load(f)
    for key,value in rows.items():
        # print(key)
        # print(value)
        items_list = value

    return render_template('items.html', items=items_list)

# function to load sql data
def load_sql_data(filename, wanted_id = None):
    """ Load SQLite data and return as dictionary """

    data = []
    where_clause = ""
    if wanted_id is not None:
        where_clause = " WHERE id = " + wanted_id

    con = sqlite3.connect(filename)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM products " + where_clause)
    rows = res.fetchall()

    # longwinded way to get a list of the col names programatically
    keys = []
    colnames = cur.description
    for desc in colnames:
        keys.append(desc[0])

    # keys = ["id", "name", "category", "price"]
    for row_tuple in rows:
        item = {}
        i = 0
        for v in row_tuple:
            item[keys[i]] = v
            i = i + 1
        data.append(item)

    # print(data)

    return data

# creates the database (only runs once, if you refresh, delete the .db file)
def create_database():
       """ creates the database """
       conn = sqlite3.connect('data/products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

@app.route('/products')
def products():
    """ renders a HTML template """
    #get the value and the id of the 'source' parameter from the URL
    source = request.args.get('source')
    id = request.args.get('id')

    #depending on source parameter read and parse data from the correspdoning file
    data = []
    if source == "json":
        data = load_json_data("data/products.json", id)
    elif source == "csv":
        data = load_csv_data("data/products.csv", id)
    elif source == "sql":
        create_database()
        data = load_sql_data("data/products.db", id)

    return render_template('product_display.html', data=data, source=source, id=id)

# function to load json data
def load_json_data(filename, wanted_id = None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)
        for row in rows:
            key = row['id']

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                product = {}
                for k,v in row.items():
                    product[k] = v
                data.append(product)

    except: ValueError("Unable to load data from file '{}'".format(filename))

    return data

# function to load csv data
def load_csv_data(filename, wanted_id = None):
    """ Load CSV data from file and returns as dictionary """

    data = []

    try:
        with open(filename, 'r') as csvfile:
            # using DictReader method to convert each row to a dictionary
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except: ValueError("Unable to load data from file '{}'".format(filename))

    return data

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
