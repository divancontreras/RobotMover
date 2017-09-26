import os
import paho.mqtt.client as paho


mqttc = paho.Client()

# Define event callbacks
def on_connect(self, mosq, obj, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

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

# Start subscribe to robot 1, with QoS level 0
mqttc.subscribe("robot/1", 0)
# Start subscribe to robot 2, with QoS level 0
mqttc.subscribe("robot/2", 0)
# Start subscribe to robot 3, with QoS level 0
mqttc.subscribe("robot/3", 0)

# Publish a STATUS
mqttc.publish("server/", "Server Online")
print("Server Online")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))