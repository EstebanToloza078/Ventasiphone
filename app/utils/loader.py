import json
import os

def get_data_path(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'data', filename)

def load_products():
    with open(get_data_path('products.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def load_promotions():
    with open(get_data_path('promotions.json'), 'r', encoding='utf-8') as f:
        return json.load(f)
