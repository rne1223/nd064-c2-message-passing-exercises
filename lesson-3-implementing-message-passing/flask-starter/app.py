#!/usr/bin/env python3

import json
from re import DEBUG
from flask import Flask, jsonify, request, flash, redirect, url_for
from datetime import datetime
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
@app.route('/neworder', methods=['POST'])
def neworder():

    data = request.get_json()
    user = data["username"]
    equipment = data["equipment"]
    now = datetime.now() 
    timestamp = now.strftime('%Y-%m-%dT%H:%M:%S.%f')

    order = {
        "created_at": timestamp,
        "created_by": user,
        "equipment": equipment 
    }

    msg = create_order(order)

    return msg ,201


if __name__ == '__main__':
    app.run(debug=True)