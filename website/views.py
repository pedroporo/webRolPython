from flask import Blueprint

vistas=Blueprint('vistas',__name__)

@vistas.route('/')
def home():
    return "<h1>Hola Pedro!</h1>"