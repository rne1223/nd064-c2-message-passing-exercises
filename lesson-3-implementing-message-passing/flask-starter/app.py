#/usr/local/env python3

from flask import Flask, jsonify, request
from datetime import datetime
import sys

# Running 'flask run'
if "run" in sys.argv:
    from .services import retrieve_orders, create_order
else: # Running 'python app.py'
    from services import retrieve_orders, create_order

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Hello world" 

@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/computers', methods=['GET'])
def getComputers():
    return jsonify(retrieve_orders())

@app.route('/api/orders/computers', methods=['POST'])
def neworder():

    data = request.values
    
    created_by = data["created_by"]
    status = data["status"]
    created_at = datetime.fromtimestamp(int(data["created_at"])).isoformat() 
    equipment =  data["equipment"]


    order = {
        "created_at": created_at,
        "created_by": created_by,
        "status": status,
        "equipment": equipment 
    }

    msg = create_order(order)

    return jsonify(msg) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)