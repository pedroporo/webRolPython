from flask import Flask
from website.MongoDB import get_connection

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'me gustan los slimes'
    from .views import vistas
    from .auth import auth
    app.register_blueprint(vistas,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app


