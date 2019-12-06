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

tokens = dict()

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


def check_token(token):
    if token in tokens:
        email = tokens[token]
        del tokens[token]
        return email
    return False


@app.route("/login", methods=["POST"])
def login():
    username = request.form['email']
    password = request.form['password']

    users = get_var('users')
    if username in users:
        if password == users[username]['password']:
            token = secrets.token_urlsafe()
            tokens[token]=username
            return jsonify({'token': token})

    return jsonify({'status': False})


@app.route("/logout/<token>", methods=["GET"])
def logout(token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    return jsonify({'status': True})

@app.route("/signup", methods=["POST"])
def signup():
    nom = request.json['nom']
    prenom = request.json['prenom']
    email = request.json['email']
    password = request.json['password']
    naissance = request.json['naissance']
    aled = request.json['aled']
    jaide = request.json['jaide']
    codepostal = request.json['codepostal']
    description = request.json['description']
    myFile = request.json['myFile']
    users = get_var('users')
    if email in users:
        return jsonify({'status': False})
    users[email] = {'nom': nom, 'prenom': prenom, 'password': password, 'naissance': naissance, 'aled': aled, 'jaide': jaide, 'codepostal': codepostal, 'description': description}
    set_var('users', users)
    token = secrets.token_urlsafe()
    tokens[token]=email
    return jsonify({'token': token})

@app.route("/matchs/<token>", methods=["GET"])
def matchs(token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    token = secrets.token_urlsafe()
    tokens[token]=res

    users = get_var('users')
    cp = users[res]['codepostal']
    matchs = dict(filter(lambda elem: elem[1]['codepostal'] == cp and elem[0] != res, users.items()))
    return jsonify({'token': token, 'matchs': matchs})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False)
    app.run(debug=True)
