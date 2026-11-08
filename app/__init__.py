from flask import Flask
import os

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    app.secret_key = os.environ.get('SECRET_KEY', 'inova-store-secret-key-demo-2026')
    app.config['JSON_AS_ASCII'] = False
    
    from app.routes.main import main
    from app.routes.api import api
    
    app.register_blueprint(main)
    app.register_blueprint(api)
    
    return app

app = create_app()
