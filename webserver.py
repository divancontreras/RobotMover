# -*- coding: utf-8 -*-
"""
Server-Side with REST API

"""

from flask import Flask, jsonify, request
import os
import paho.mqtt.client as paho


mqttc = paho.Client()
# Connect
mqttc.username_pw_set("izcgxpdo", "ueK_f21lpCto")
mqttc.connect('m12.cloudmqtt.com', 12583)

mqttc.publish("server/", "Server Online")

app = Flask(__name__)

# def parseToString(data):
#     strdata = data['command'] + "," + data['stateid'] + "," + data['robotid'] + "," + data['payload']
#     return strdata

@app.route('/', methods = ['POST', 'GET'])
def root():

    content = request.get_json()
    if(not 'command' in content):
        return 'Missing {command}', 500
    elif(not 'stateid' in content):
        return 'Missing {stateid}', 500
    elif(not 'robotid' in content):
        return 'Missing {robotid}', 500
    elif(not 'payload' in content):
        return 'Missing {payload}', 500

    result, mid = mqttc.publish("robot/" + content['robotid'], jsonify(content))
    if result == paho.MQTT_ERR_SUCCESS:
        return jsonify(content), 200
    
    return "WIERD ERROR", 500
    # try:
        
    # except:
    #     return "NOT A JSON", 500
