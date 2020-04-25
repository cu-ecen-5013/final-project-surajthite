import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import datetime

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

datetime_object = datetime.datetime.now() 
  
def on_message(client, userdata, msg):
  a=msg.payload.decode()
  print(datetime_object)
  print("Current Temperature is - - ->: %s" %a)

  
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()