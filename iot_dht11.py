#!/usr/bin/python
# name: iot_dht11.py
# desc: iot sessor: (dht11, dht22) to collect temp, humidity using python
#
# usage: python iot_dht11.py
#
# prerequisites:
# 1. Install needed python modules - see the import statements below.
# 2. This program writes output as JSON to a linux file in directory my_dir. 
#         If you wish to write to a differ directory, update
#         these fields with your information:
#             a. my_dir
#             b. (optional) out_file, state
#######################################################
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import math
import os.path
#######################################################
# Variables are here
#######################################################
# WARNING for WINDOWS users. If you are changing the 
#    my_dir directory to a WINDOWS directory, the
#    directory seperator in python is 2 backslashes.
#    This script is set up for linux, which uses the 
#    forward slash (only needs one). As python sees 
#    the WINDOWS backslash as a command not to "eat"
#    the character following it, we use 2 backslashes
#    for WINDOWS paths and directories
#        example: C:\\users\\YOUR_USER\\desktop\\my_file
#-----------------------------------------------------#
my_dir="/tmp"                               #Directory to hold out_file and state_file
out_file="dht11.out"                        #The output data file holding your data
state_file="state"                          #The file holding the weather forecast or current state
#
# Variable - Sensor you are using
#
using_DHT11_sensor = 11                     #Use this variable if using DHT11 sensor (default)
                                            #  --> See line below starting with humidity, temperture
using_DHT22_sensor = 22                     #use this variable if using DHT22 sensor
                                            #  --> See line below starting with humidity, temperture
my_gpio_pin_for_sensor = 4                  #RPi uses this GPIO pin for sensor data
#######################################################
# MAIN Logic starts here
#######################################################
GPIO.setmode(GPIO.BOARD)                    #Tell RPi we are using GPIO naming convention

#state = os.system('python irrigation.py')  #Uncomment this line if you want the weather
                                            #forecast included in output - writes to state
                                            #field, other defaults to "0". Must have 
                                            #program irrigation.py in the SAME directory 
                                            #as this program. See irrigation.py for setting
                                            #up with your personal information - such as the weather.
if os.path.isfile(my_dir + "/" + state_file): #This if statement will bring in the 
                                              #    the updated weather forecast, if 
                                              #    you uncommented out the line starting
                                              #    with state.
    file = open(my_dir + "/" + state_file, "r")
    state = file.read() 
else:
    file = open(my_dir + "/ " + state_file, "w")
    file.write("0")
    state = 0

file.close()
if state == "":                             #Just in case we have garbage, then default state to 0
    state = 0

humidity, temperature = Adafruit_DHT.read_retry(using_DHT22_sensor, my_gpio_pin_for_sensor) #Read the sensor 

temperature = ((temperature*1.8) + 32)      #Convert celsius to fahrenheit
file = open(my_dir + "/" + out_file,"w")    #Open the out_file
file.write('{{"temp":{}'.format(temperature) + ',"hum":{:g}'.format(humidity) + ',"state":"{}"'.format(state) + '}' ) #write data to out_file
file.close()                                #Close and end processsing - we are done.

