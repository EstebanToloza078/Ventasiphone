from flask import Blueprint, render_template, request, jsonify, session
from app.utils.loader import load_products, load_promotions

main = Blueprint('main', __name__)

@main.route('/')
def home():
    products = load_products()
    promotions = load_promotions()
    featured = [p for p in products if p.get('featured', False)][:8]
    return render_template('index.html', products=featured, promotions=promotions, all_products=products)

@main.route('/catalogo')
def catalog():
    products = load_products()
    q = (request.args.get('q') or '').strip().lower()
    category = (request.args.get('category') or '').strip().lower()

    filtered = products
    if q:
        def matches(p):
            hay = ' '.join([
                str(p.get('name', '')),
                str(p.get('model', '')),
                str(p.get('generation', '')),
                str(p.get('id', '')),
                str(p.get('brand', '')),
                str(p.get('category', '')),
            ]).lower()
            return q in hay or q.replace(' ', '') in hay.replace(' ', '')
        filtered = [p for p in filtered if matches(p)]

    if category == 'accesorios':
        filtered = [p for p in filtered if str(p.get('category', '')).lower() == 'accesorios']
    elif category == 'iphone-pro':
        filtered = [p for p in filtered if 'pro' in str(p.get('model', '')).lower() and 'max' not in str(p.get('model', '')).lower()]
    elif category == 'iphone-promax':
        filtered = [p for p in filtered if 'pro max' in str(p.get('model', '')).lower()]
    elif category == 'economicos':
        # show lower-priced options (by first variant price)
        def price_of(p):
            vs = p.get('variants') or []
            return vs[0].get('price', 10**12) if vs else 10**12
        filtered = sorted(filtered, key=price_of)[:8]
    elif category == 'anteriores':
        filtered = [p for p in filtered if str(p.get('generation', '')).isdigit() and int(p.get('generation', 99)) <= 15]

    return render_template('catalog.html', products=filtered, q=request.args.get('q',''), category=request.args.get('category',''))

@main.route('/producto/<product_id>')
def product_detail(product_id):
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return 'Producto no encontrado', 404
    related = [p for p in products if p['id'] != product_id and p['brand'] == product['brand']][:4]
    return render_template('product_detail.html', product=product, related=related)

@main.route('/carrito')
def cart():
    return render_template('cart.html')

@main.route('/checkout')
def checkout():
    return render_template('checkout.html')

@main.route('/ofertas')
def offers():
    products = load_products()
    offers = [p for p in products if p.get('discount') and p['discount'] > 0]
    return render_template('offers.html', products=offers)

@main.route('/contacto')
def contact():
    return render_template('contact.html')
