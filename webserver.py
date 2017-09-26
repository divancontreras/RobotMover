# -*- coding: utf-8 -*-
"""
Server-Side with REST API

"""

from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/', methods = ['POST'])
def root():
    content = request.get_json()
    if('command' in content):
        return 'Missing {command}', 500
    if('stateID' in content):
        return 'Missing {stateID}', 500
    if('robotID' in content):
        return 'Missing {robotID}', 500
    if('payload' in content):
        return 'Missing {payload}', 500

    return jsonify(content), 200
