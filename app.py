import datetime
import requests
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from time import time
import re
import os
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
            tokens[token] = username
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
    users = get_var('users')
    if email in users:
        return jsonify({'status': False})
    users[email] = {'likes': list(), 'dislikes': list(), 'nom': nom, 'prenom': prenom, 'password': password,
                    'naissance': naissance, 'aled': aled, 'jaide': jaide, 'codepostal': codepostal,
                    'description': description, 'pdp': '../static/img/symbole3.svg'}
    set_var('users', users)
    token = secrets.token_urlsafe()
    tokens[token] = email
    return jsonify({'token': token})


@app.route("/signup/<email>", methods=["POST"])
def signup_pdp(email):
    file = request.files['file']
    name, ext = os.path.splitext(file.filename)
    filename = secrets.token_urlsafe() + ext
    file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'upload', filename))

    users = get_var('users')
    if email in users:
        users[email]['pdp'] = filename
        set_var('users', users)
        return jsonify({'status': True})
    return jsonify({'status': False})


@app.route("/tinder/<token>", methods=["GET"])
def tinder(token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    token = secrets.token_urlsafe()
    tokens[token] = res

    users = get_var('users')
    user = users[res]
    cp = user['codepostal']
    likes = user['likes']
    dislikes = user['dislikes']
    tinders = dict(filter(lambda elem: elem[1]['codepostal'] == cp and elem[0] != res and elem[0] not in likes and elem[
        0] not in dislikes, users.items()))
    return jsonify({'token': token, 'tinder': tinders})


@app.route("/like/<email>/<token>", methods=["GET"])
def like(email, token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    token = secrets.token_urlsafe()
    tokens[token] = res

    users = get_var('users')
    users[res]['likes'].append(email)
    set_var('users', users)
    return jsonify({'token': token, 'status': True})


@app.route("/dislike/<email>/<token>", methods=["GET"])
def dislike(email, token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    token = secrets.token_urlsafe()
    tokens[token] = res

    users = get_var('users')
    users[res]['dislikes'].append(email)
    set_var('users', users)
    return jsonify({'token': token, 'status': True})


@app.route("/matchs/<token>", methods=["GET"])
def matchs(token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    token = secrets.token_urlsafe()
    tokens[token] = res

    users = get_var('users')
    user = users[res]
    likes = user['likes']
    matchs = dict(filter(lambda elem: elem[0] in likes and res in elem[1]['likes'], users.items()))
    return jsonify({'token': token, 'matchs': matchs})


# TODO
@app.route("/send/<token>", methods=["POST"])
def send(token):
    res = check_token(token)
    if res == False:
        return jsonify({'status': False})
    token = secrets.token_urlsafe()
    tokens[token] = res

    email = request.json['email']
    message = request.json['message']
    messages = get_var('messages')

    return jsonify({'token': token})


@app.route("/secret", methods=["GET"])
def secret():
    return send_from_directory('static', 'secret.html')


@app.route("/secret_verif", methods=["GET"])
def secret_verif():
    code = request.args['code']
    if code == '1435':
        return send_from_directory('static', 'ouvert.html')
    return send_from_directory('static', 'lose.html')


@app.route("/upload/<name>", methods=["GET"])
def photo(name):
    return send_from_directory('upload', name)


@app.route("/<name>", methods=["GET"])
def root_serve(name):
    return send_from_directory('.', name)


@app.route("/", methods=["GET"])
def main_page():
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
