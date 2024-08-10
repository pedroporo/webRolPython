from flask import Blueprint, g, session, redirect, request, url_for, jsonify, render_template,make_response
import os,json
from requests_oauthlib import OAuth2Session

DISCORD_OAUTH2_CLIENT_ID = '1271387380489781299'
DISCORD_OAUTH2_CLIENT_SECRET = 'tQEO3hIIahjwo8Z4lb8I8G5NxWigtin2'
DISCORD_OAUTH2_REDIRECT_URI = 'http://localhost:5000/callback'

API_BASE_URL = os.environ.get('API_BASE_URL', 'https://discordapp.com/api')
AUTHORIZATION_BASE_URL = API_BASE_URL + '/oauth2/authorize'
TOKEN_URL = API_BASE_URL + '/oauth2/token'





auth=Blueprint('auth',__name__)

if 'http://' in DISCORD_OAUTH2_REDIRECT_URI:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'


def token_updater(token):
    session['oauth2_token'] = token

def create_session(token=None, state=None, scope=None):
    return OAuth2Session(
        client_id=DISCORD_OAUTH2_CLIENT_ID,
        token=token,
        state=state,
        scope=scope,
        redirect_uri=DISCORD_OAUTH2_REDIRECT_URI,
        auto_refresh_kwargs={
            'client_id': DISCORD_OAUTH2_CLIENT_ID,
            'client_secret': DISCORD_OAUTH2_CLIENT_SECRET,
        },
        auto_refresh_url=TOKEN_URL,
        token_updater=token_updater)


@auth.route('/login')
def login():
    scope = request.args.get(
        'scope',
        'identify')
    discord = create_session(scope=scope.split(' '))
    authorization_url, state = discord.authorization_url(AUTHORIZATION_BASE_URL)
    session['oauth2_state'] = state
    print("authorization_url", authorization_url)
    return redirect(authorization_url)

@auth.route('/callback')
def callback():
    if request.values.get('error'):
        return redirect('/')
    discord = create_session(state=session.get('oauth2_state'))
    token = discord.fetch_token(
        TOKEN_URL,
        client_secret=DISCORD_OAUTH2_CLIENT_SECRET,
        authorization_response=request.url)
    #print("test")
    session['oauth2_token'] = token
    #print(session.get('oauth2_token'))
    discord = create_session(token=session.get('oauth2_token'))
    user_details = discord.get(API_BASE_URL + '/users/@me').json()
    #return render_template("home.html",user=user_details)
    #return redirect('/',user_details=user_details)
    user_details_json = json.dumps(user_details)
    resp=make_response(redirect('/'))
    resp.set_cookie('user_details_json',user_details_json)
    return resp

@auth.route('/logout')
def logout():
    resp=make_response(redirect('/'))
    resp.set_cookie('user_details','',expires=0)
    resp.set_cookie('user_details_json','',expires=0)
    return resp