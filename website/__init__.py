from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'me gustan los slimes'
    from .views import vistas
    from .auth import auth
    app.register_blueprint(vistas,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app


