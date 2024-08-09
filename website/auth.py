from flask import Blueprint
import os

DISCORD_OAUTH2_CLIENT_ID = '761778934848421929'
DISCORD_OAUTH2_CLIENT_SECRET = 'PTKRYcJ2HdnlRkYoU7ShQw8VU-IPz5an'
DISCORD_OAUTH2_REDIRECT_URI = 'http://localhost:5000/callback'

API_BASE_URL = os.environ.get('API_BASE_URL', 'https://discordapp.com/api')
AUTHORIZATION_BASE_URL = API_BASE_URL + '/oauth2/authorize'
TOKEN_URL = API_BASE_URL + '/oauth2/token'






auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<h1>Login!</h1>"


@auth.route('/logout')
def logout():
    return "<h1>Cerrar sesion!</h1>"