import os
import paho.mqtt.client as paho
import json
import requests

mqttc = paho.Client()

# Define event callbacks
def on_connect(self, mosq, obj, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    jsonData = str(msg.payload).replace("'",'"')
    print(str(jsonData)) 
    try:
        jsonData = json.loads(str(jsonData))
    except:
        jsonData = json.dumps({"error" : "not a json"})
        if '/' in str(msg.topic):
            jsonData = json.dumps(jsonData,{"robotid": msg.topic.split('/')[1]})
        else:
            jsonData = json.dumps(jsonData,{"robotid" : "No robot id specified"})
    print(jsonData)

    r = requests.post('http://48b0a7da.ngrok.io/notify', data=jsonData, verify=False)  
    print("Se mando")
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