from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import products_dao
import uom_dao
import order_dao
from sql_connection import get_sql_connection

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_all_products():
    products = products_dao.get_all_products(connection)
    return jsonify(products)

@app.route('/getUOM', methods=['GET'])
def get_uom():
    uoms = uom_dao.get_uoms(connection)
    return jsonify(uoms)

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = request.get_json()
    product_id = products_dao.insert_new_product(connection, request_payload)
    return jsonify({'product_id': product_id})

@app.route('/updateProduct', methods=['POST'])
def update_product():
    request_payload = request.get_json()
    updated_id = products_dao.update_product(connection, request_payload)
    return jsonify({'product_id': updated_id})

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    request_payload = request.get_json()
    products_dao.delete_product(connection, request_payload['product_id'])
    return jsonify({'status': 'success'})

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = request.get_json()
    order_id = order_dao.insert_order(connection, request_payload)
    return jsonify({'order_id': order_id})

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    orders = order_dao.get_all_orders(connection)
    return jsonify(orders)

@app.route('/getOrderDetails', methods=['GET'])
def get_order_details():
    order_id = request.args.get('order_id')
    if not order_id:
        return jsonify({'error': 'order_id is required'}), 400
    order_details = order_dao.get_order_details(connection, order_id)
    return jsonify(order_details)

if __name__ == '__main__':
    from waitress import serve
    import os

    port = int(os.environ.get('PORT', 5000))
    print(f"Server started for Cloud Kitchen App on port {port}")
    serve(app, host='0.0.0.0', port=port)

