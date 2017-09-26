import os
import paho.mqtt.client as paho
import json
from pprint import pprint
import requests

mqttc = paho.Client()

# Define event callbacks
def on_connect(self, mosq, obj, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    r = requests.post('http://mockbin.org/bin/c67f373e-e0a3-46e1-91e3-02b9c7e9f91e?foo=bar&foo=baz', data=parseInput(msg), verify=False)
    #req = urllib2.Request('https://requestb.in/stjgqast')
    #req.add_header('Content-Type', 'application/json')
    #response = urllib2.urlopen(req, parseInput(msg))   

def parseInput(msg):
    #Check that string is not empty
    smsg = str(msg.payload)
    # Something a b' appears on the object msg.payload, so, a condition
    if 'b\'' in smsg :
        message = str(msg.payload)[2:len(smsg)-1]
        message = message.split(',')
        return genJson(message)
    elif len(smsg) == 0 :
        return json.dumps('')
    else:
        message = smsg.split(',')
        return genJson(message)

def genJson(msg):
    data = {
	"orden": msg[0],
	"stateid": msg[1],
	"robotid": msg[2],
	"payload": msg[3]}
    return json.dumps(data)


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
mqttc.on_log = on_log

# Connect
mqttc.username_pw_set("izcgxpdo", "ueK_f21lpCto")
mqttc.connect('m12.cloudmqtt.com', 12583)

# Start subscribe, with QoS level 0
#mqttc.subscribe("hello/world", 0)
mqttc.subscribe("robot/1", 0)
mqttc.subscribe("robot/2", 0)
mqttc.subscribe("robot/3", 0)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))