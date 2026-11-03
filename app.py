from flask import Flask, render_template, request, jsonify, session
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'inova-store-secret-key-demo-2026'
app.config['JSON_AS_ASCII'] = False

# Load product data
def load_products():
    with open('data/products.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_promotions():
    with open('data/promotions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    products = load_products()
    promotions = load_promotions()
    # Get featured products
    featured = [p for p in products if p.get('featured', False)][:8]
    return render_template('index.html', products=featured, promotions=promotions, all_products=products)

@app.route('/catalogo')
def catalog():
    products = load_products()
    return render_template('catalog.html', products=products)

@app.route('/producto/<product_id>')
def product_detail(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return 'Producto no encontrado', 404
    # Get related products (same model family)
    related = [p for p in products if p['id'] != product_id and p['brand'] == product['brand']][:4]
    return render_template('product_detail.html', product=product, related=related)

@app.route('/carrito')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/ofertas')
def offers():
    products = load_products()
    offers = [p for p in products if p.get('discount') and p['discount'] > 0]
    return render_template('offers.html', products=offers)

@app.route('/contacto')
def contact():
    return render_template('contact.html')

@app.route('/api/products')
def api_products():
    products = load_products()
    return jsonify(products)

@app.route('/api/product/<product_id>')
def api_product(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(product)

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    if 'cart' not in session:
        session['cart'] = []
    
    cart = session['cart']
    # Check if item with same product_id, color, capacity exists
    for item in cart:
        if item['product_id'] == data['product_id'] and item['color'] == data['color'] and item['capacity'] == data['capacity']:
            item['quantity'] += data.get('quantity', 1)
            session.modified = True
            return jsonify({'success': True, 'cart': cart})
    
    cart.append(data)
    session.modified = True
    return jsonify({'success': True, 'cart': cart})

@app.route('/api/cart')
def get_cart():
    return jsonify(session.get('cart', []))

@app.route('/api/cart/update', methods=['POST'])
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

@app.route('/api/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    cart = session.get('cart', [])
    cart = [item for item in cart if not (item['product_id'] == data['product_id'] and item['color'] == data['color'] and item['capacity'] == data['capacity'])]
    session['cart'] = cart
    session.modified = True
    return jsonify({'success': True, 'cart': cart})

@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    session['cart'] = []
    session.modified = True
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
