from flask import Blueprint,render_template

vistas=Blueprint('vistas',__name__)

@vistas.route('/')
def home():
    return render_template("home.html")