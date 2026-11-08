from flask import Blueprint, request, jsonify, session
from app.utils.loader import load_products

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/products')
def api_products():
    products = load_products()
    return jsonify(products)

@api.route('/product/<product_id>')
def api_product(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(product)

@api.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    if 'cart' not in session:
        session['cart'] = []
    cart = session['cart']
    for item in cart:
        if item['product_id'] == data['product_id'] and item['color'] == data['color'] and item['capacity'] == data['capacity']:
            item['quantity'] += data.get('quantity', 1)
            session.modified = True
            return jsonify({'success': True, 'cart': cart})
    cart.append(data)
    session.modified = True
    return jsonify({'success': True, 'cart': cart})

@api.route('/cart')
def get_cart():
    return jsonify(session.get('cart', []))

@api.route('/cart/update', methods=['POST'])
def update_cart():
    data = request.get_json()
    cart = session.get('cart', [])
    for item in cart:
        if item['product_id'] == data['product_id'] and item['color'] == data['color'] and item['capacity'] == data['capacity']:
            item['quantity'] = data['quantity']
            break
    session['cart'] = cart
    session.modified = True
    return jsonify({'success': True, 'cart': cart})

@api.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    cart = session.get('cart', [])
    cart = [item for item in cart if not (item['product_id'] == data['product_id'] and item['color'] == data['color'] and item['capacity'] == data['capacity'])]
    session['cart'] = cart
    session.modified = True
    return jsonify({'success': True, 'cart': cart})

@api.route('/cart/clear', methods=['POST'])
def clear_cart():
    session['cart'] = []
    session.modified = True
    return jsonify({'success': True})
