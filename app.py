import datetime
import requests
from flask import Flask, request, jsonify
from time import time
import re
import json
import csv
from meteocalc import Temp, heat_index
from xlrd.xldate import xldate_from_datetime_tuple
import secrets

app = Flask(__name__)

users = dict()
users['admin'] = 'azerty'
tokens = list()

def set_var(name, value):
    with open('vars.txt', 'r') as file:
        my_vars = json.load(file)
    my_vars[name] = value
    with open('vars.txt', 'w') as file:
        json.dump(my_vars, file, indent=2)


def get_var(name):
    with open('vars.txt', 'r') as f:
        variables = json.load(f)
    try:
        return variables[name]
    except KeyError:
        return None


def check_token():
    req = request.get_json()
    if req is None or 'token' not in req:
        return jsonify({'message': 'Token needed'})
    token = req['token']
    if token in tokens:
        tokens.remove(token)
        return True
    return jsonify({'message': 'Bad token'})


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
    username = request.get_json()['username']
    password = request.get_json()['password']

    if username in users:
        if password == users[username]:
            token = secrets.token_urlsafe()
            tokens.append(token)
            return jsonify({'token': token, 'message': 'Login successful'})

    return jsonify({'message': 'Login failed'})


@app.route("/logout", methods=["POST"])
def logout():
    res = check_token()
    if res == True:
        return jsonify({'message': 'Logged out'})
    return res

@app.route("/signup", methods=["POST"])
def signup():
    projectpath = request.form['projectFilezpath']
    return ''


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False)
    app.run(debug=False)
