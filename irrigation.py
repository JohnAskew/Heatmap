#!/usr/bin/python
# ManhLab applications circa 2018, 2019
# Beer-ware, so under GNU open licensing, 
# free to modify and reuse at will. We are 
# unable to charge for this script. 
# The script is free and open. We do charge by the bug.... 
#
### BEGIN SERIOUS CONTENT HERE ####

import sys, os
from datetime import datetime, time
import paho.mqtt.client as mqtt
from weatherbit.api import Api
#
# Housekeeping, remove any preexisting files
#
if os.path.exists("/tmp/temp"):
    os.remove("/tmp/temp")
if os.path.exists("/tmp/hum"):
    os.remove("/tmp/hum")
if os.path.exists("/tmp/state"):
    os.remove("/tmp/state")

#Register ManhLab at weatherbit.io to get an API key
api_key = "your-registration-key-goes-here"

#Find your Latitude and Longitude here: https://www.latlong.net/
lat = 32.648997
lon = -80.487985
unit = 'I'

#rainy/wet weather codes
codes=[  200, 201, 202, 230, 231, 232, 233, 300, 301, 302, 500, 501, 502, 511, 520, 521, 522]

#set the API key
api = Api(api_key)


# Set the granularity of the API - Options: ['daily','hourly','3hourly']
# Will only affect forecast requests.
api.set_granularity('daily')
#DEBUG api.set_granularity('hourly')
# Query by lat/lon
forecast = api.get_forecast(lat=lat, lon=lon, units=unit)
#
# Format the returned weather json to extract desired information 
#
precipMM = forecast.get_series(['precip'])[0]['precip']
weatherCode = forecast.get_series(['weather'])[0]['weather']['code']
date0 = datetime.now().strftime("%Y%m%d%H%M%S").replace('\'', '"') 
temp0 = forecast.get_series(['temp'])[0]['temp']
hum0  = forecast.get_series(['rh'])[0]['rh']
condition = forecast.get_series(['weather'])[0]['weather']['description']
#
#DEBUGprint(weatherCode)
print(date0, temp0, hum0, condition)
#DEBUG print(precipMM)
#
# Prepare to write the output to /tmp to persist for dht11.py to pick up
#
file_temp = open("/tmp/temp","w")
file_hum = open("/tmp/hum","w")
file = open("/tmp/state","w")
#
# search the returned weather json for rain codes and write to file we opened.
#
for code in codes:
        file_temp.write('{}'.format(temp0))
        file_hum.write('{}'.format(hum0))
	#if the day's code matches a known wet day, cancel watering for the day
	if weatherCode == code or precipMM > 3.0:
		file.write('rain')
        else: 
            file.write(condition.replace(" ", "_"))

        file.close()
        file_hum.close()
        file_temp.close()
        sys.exit()
