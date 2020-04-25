# FileName: Client-Publisher.py
# Author: Suraj Thite
# Description: This python script runs as mqtt client
# Reference: https://github.com/eclipse/paho.mqtt.python


import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import sys
import urllib2

from datetime import datetime
print("**************Sending temperature to MQTT Server*****************")
#print 'Argument List:', str(sys.argv)
client = mqtt.Client()
client.connect("10.0.0.20",1883,60)
#x=raw_input();
print(sys.argv[1])
#d_t = str(datetime.now())
#print(d_t)

now = datetime.now() 
#print("now =", now)

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("date and time = " + dt_string)	

curr_date = now.strftime("%m/%d/%Y")
curr_time = now.strftime("%H:%M:%S")

temp_value = sys.argv[1].split(":")[1]
temp_value = temp_value[:5] + " C"


# data_to_send = dt_string + str(sys.argv[1])

#data_to_send = dt_string + " " + temp_value

data_to_send = "| " + curr_date + " | " + curr_time + " | " + " " + temp_value + " |"

#data_to_send_2 = "____________________________________"

def internet_on():
    try:
        urllib2.urlopen('http://10.0.0.20', timeout=1)
        print("**************Connected to server***********************")
	client.publish("topic/test",data_to_send)
    except urllib2.URLError as err: 
        print("**************Disconnected from Server******************")
	file_handler = open('/usr/tmp102_backup.txt', 'a')
	file_handler.write(data_to_send)
  	file_handler.write("\n")
  	file_handler.close()

internet_on()
#client.publish("topic/test",data_to_send)
#client.publish("topic/test",data_to_send_2)
#client.publish("topic/test",str(sys.argv[1]))
print(sys.argv[1])
client.disconnect();

