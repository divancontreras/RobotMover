import os
import paho.mqtt.client as paho
import json
from pprint import pprint

mqttc = paho.Client()

# Define event callbacks
def on_connect(self, mosq, obj, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
	print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
	jsonfile = parseInput(msg)

def parseInput(msg):
    smsg = str(msg.payload)
    if(len(smsg) > 3):
    	message = str(msg.payload)[2:len(smsg)-1]
    	message = message.split(',')
    	return genJson(message)

def genJson(msg):
	data = {
	"orden": msg[0],
	"stateid": msg[1],
	"robotid": msg[2],
	"positions": msg[3]}
	return json.dumps(data)


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

def parseToString():
	#Agregar URL del .json
	with open('dummmy.json') as data_file:    
	    data = json.load(data_file)
	    strdata = data['orden'] + "," + data['stateid'] + "," + data['robotid'] + "," + data['positions']
	    return strdata


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
mqttc.subscribe("hello/world", 0)

# Publish a message
mqttc.publish("hello/world", "s,2,b,53")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))