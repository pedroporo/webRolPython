from flask import Blueprint,render_template,request,jsonify
import json

vistas=Blueprint('vistas',__name__)

@vistas.route('/')
def home():
    user_details_json=request.cookies.get('user_details_json')
    if user_details_json is not None:
        user_details = json.loads(user_details_json)
        return render_template("home.html",user=user_details)
    return render_template("home.html",user=user_details_json)