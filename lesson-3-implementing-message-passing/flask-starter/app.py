#!/usr/bin/env python3

import json
from re import DEBUG
from flask import Flask, jsonify, request, flash, redirect, url_for
from pprint import pprint

from services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/')
def main_page():
    return redirect(url_for('orders'))

@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/orders')
def getOrders():
    return json.dumps(retrieve_orders()), 200, {'Content-Type': 'application/json'}

# Define the post creation functionality 
@app.route('/neworder', methods=('GET', 'POST'))
def neworder():

    response = '' 

    # if request.method == 'POST':
    #     response = json.dumps({"data": request.data})

    pprint(request.values)
    return "hi " ,200

    #     content = request.form['content']

    #     if not title:
    #         flash('Title is required!')
    #     else:
    #         # Insert into the order
    #         return redirect(url_for('index'))

    # return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
