import datetime
import requests
from flask import Flask, request, jsonify
from time import time
import re
import json
from xlrd.xldate import xldate_from_datetime_tuple
import secrets

app = Flask(__name__)

db_file = 'C:\\Users\\jojo5\\Desktop\\StarLog\\vars.txt'

tokens = list()

def set_var(name, value):
    with open(db_file, 'r') as file:
        my_vars = json.load(file)
    my_vars[name] = value
    with open(db_file, 'w') as file:
        json.dump(my_vars, file, indent=2)


def get_var(name):
    with open(db_file, 'r') as f:
        variables = json.load(f)
    try:
        return variables[name]
    except KeyError:
        return None


def check_token():
    req = request.get_json()
    if req is None or 'token' not in req:
        return jsonify({'status': False})
    token = req['token']
    if token in tokens:
        tokens.remove(token)
        return True
    return jsonify({'status': False})


@app.route('/', methods=["GET"])
def home():
    res = check_token()
    if res == True:
        token = secrets.token_urlsafe()
        tokens.append(token)
        return jsonify({'token': token, 'message': 'accès accordé'})
    return res


@app.route("/login", methods=["POST"])
def login():
    username = request.form['email']
    password = request.form['password']

    users = get_var('users')
    if username in users:
        if password == users[username]:
            token = secrets.token_urlsafe()
            tokens.append(token)
            return jsonify({'token': token})

    return jsonify({'status': False})


@app.route("/logout", methods=["POST"])
def logout():
    res = check_token()
    if res == True:
        return jsonify({'status': True})
    return res

@app.route("/signup", methods=["POST"])
def signup():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    password = request.form['password']
    naissance = request.form['naissance']
    aled = request.form['aled']
    myFile = request.form['myFile']
    users = get_var('users')
    if email in users:
        return jsonify({'status': False})
    users[email] = {'nom': nom, 'prenom': prenom, 'password': password, 'naissance': naissance, 'aled': aled}
    set_var('users', users)
    token = secrets.token_urlsafe()
    tokens.append(token)
    return jsonify({'token': token})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False)
    app.run(debug=True)
