#!/usr/bin/python
# Let's do our best to be Pythonic - hence the comments.
import bluetooth._bluetooth as bt
import commands
import datetime  
import Adafruit_DHT
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os.path
import sys
''' name: swat_temp_pub.py 
    desc: will grab the weather from irrigation.py 
    if it is uncommented.  Basic functionality is to read 
    the DHT11 or DHT22 and derive the temp and humidity.
    The script goes onto capture the current time and the 
    device bluetooth mac address and generates a json line, 
    worthy of publishing to the cloud.
    usage: python swat_temp_pub.py
   ''' 
#--------------------------------------#
# Raspberry PI Sensor Set up Here
#--------------------------------------#
GPIO.setmode(GPIO.BOARD)               #Tell RasPi we are using GPIO not pin#
myGpio = 4                             #Tell RasPI which GPIO is for the sensor line
mySensor = 22                          #Tell Raspi using DHT-22 not DHT-11 - which has value 11.
#--------------------------------------#
### Set home_path and load MQTT password located in home_path.
#--------------------------------------#
home_dir = '/home/jaskew/scripts/python'
if os.path.isdir(home_dir):
    os.chdir(home_dir)
else:
    home_dir = './'
with open(".mqtt_pw", 'r') as file:
    my_key = file.read()
    my_key = my_key[:-1]
    print(my_key)
file.close()
#--------------------------------------#
# MQTT Info
#--------------------------------------#
myUsername="jaskew"
myServer="96.80.44.170"
myPort=8883
myTopic="myTopic/To/Sensors/lr"
myClient = mqtt.Client("rhea-200")
myClient.username_pw_set(username=myUsername,password=my_key)
myClient.connect(myServer, myPort, keepalive=60, bind_address="")
##
### The next step is optional. You can comment out and simply default to a state of 0
###  instead of allowing irrigation.py to set state to the current forecast.
##
state = os.system('python /home/jaskew/scripts/python/irrigation.py')
##
### Read the state file, and use if it contains valid data, 
###   otherwise, set it to zero and publish lineitem with state 0.
##
if os.path.isfile("/tmp/state"):
    file = open("/tmp/state", "r")
    state = file.read() 
else:
    file = open("/tmp/state", "w")
    file.write("0")

file.close()
if state == "":
    state = 0
##
### Get the bluetooth mac address
##
cmd = "hciconfig"
device_id = "hci0" 
status, output = commands.getstatusoutput(cmd)
bt_mac = output.split("{}:".format(device_id))[1].split("BD Address: ")[1].split(" ")[0].strip()
##
### Get the current time
##
date0 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
##
### Get the temp and humidity
##
humidity, temperature = Adafruit_DHT.read_retry(mySensor, myGpio)
temperature = ((temperature*1.8) + 32)
##
### Write file 
##
myLine=('{"device":"' + bt_mac + '\","sysdate":"' + date0 + '\",\"temp":{:g}'.format(temperature) + ',"hum":{:g}'.format(humidity) + ',"state":"{}"'.format(state) + '}' )
file = open("/tmp/dht11.out","w")
file.write('{"device":"' + bt_mac + '\","sysdate":"' + date0 + '\",\"temp":{:g}'.format(temperature) + ',"hum":{:g}'.format(humidity) + ',"state":"{}"'.format(state) + '}' ) #',"state":0 }}}' )
file.close()
myClient.publish(myTopic, myLine)

