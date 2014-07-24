import datetime
import hashlib
import string,random  
 
# config file
import config
 
from flask import Flask, jsonify, request
 
## app and db is defined on model.py 
from model import db, app, Player
 
# other misc functions
def get_user_id(username): 
    p  = Player.query.filter_by(username=username).first()
    if p  is not None: 
       return p
    return None
 
def get_userid_by_email(email): 
    p  = Player.query.filter_by(email=email).first()
    if p  is not None: 
       return p
    return None
 
def get_user_key(key): 
    p  = Player.query.filter_by(activation_key=key).first()
    if p  is not None: 
       return p
    return None
 
 
# url  routing
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
 
@app.after_request
def shutdown_session(response):
    db.session.remove()
    return response
 
@app.route('/')
def hello_world():
    return "Hello World!"
 
@app.route('/users/')
def list_players():
    players = Player.query.all()
    
    a = "xxx";
    d = {} 
    for p in players: 
       app.logger.debug(p.username)
       a = a + " " + p.username 
    return "Hello Players: %s "  % (a)
 
  
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')