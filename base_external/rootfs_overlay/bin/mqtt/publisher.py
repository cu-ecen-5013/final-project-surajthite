# FileName: Client-Publisher.py
# Author: Suraj Thite
# Description: This python script runs as mqtt client
# Reference: https://github.com/eclipse/paho.mqtt.python


import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import sys
import urllib2
import socket
import os
from datetime import datetime

print("**************Sending temperature to MQTT Server*****************")
client = mqtt.Client()
now = datetime.now() 
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("date and time = " + dt_string)	
curr_date = now.strftime("%m/%d/%Y")
curr_time = now.strftime("%H:%M:%S")
temp_value = sys.argv[1].split(":")[1]
temp_value = temp_value[:5] + " C"

data_to_send = "T1                 |        " + curr_date + "--" + curr_time + "        | " + "       " + temp_value + "     |"

server_ip = '10.0.0.20 -s 1 -c 1 -q'
def internet_on():
  
	print("**************Pinging to Server******************")
	rep = os.system('ping ' + server_ip)
	if rep == 0:
 	 print("**************Ping Successful to server***********************")
 	 client.connect("10.0.0.20",1883,60) 
	 client.publish("topic/test",data_to_send)
	else:
	 print("**************Writing to BackUp file******************")
	 file_handler = open('/usr/tmp102_backup.txt', 'a')
	 file_handler.write(data_to_send)
  	 file_handler.write("\n")
  	 file_handler.close()

internet_on()
#client.publish("topic/test",data_to_send)
#client.publish("topic/test",data_to_send_2)
#client.publish("topic/test",str(sys.argv[1]))
print('Current Data Point | ' + sys.argv[1])
client.disconnect();
