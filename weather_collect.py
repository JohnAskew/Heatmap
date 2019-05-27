import geocoder
import requests
import datetime
import os
 
home_dir = '/home/jaskew/script/python'

if os.path.isdir(home_dir):
    os.chdir(homedir)
else:
    home_dir = './'

with open("api_key", 'r') as file:
    my_key = file.read()
    my_key = my_key[:-1]
file.close()
dark_sky="https://api.darksky.net/forecast/"
lat=0
lng=0
url=""
weather = {}
forecast = {}
currently = ""
temp = ""
now = datetime.datetime.now()
file = open("/home/jaskew/weather_collect.txt" , "a+")


destinations = ['2702 Huntingdon Chase Atlanta Georgia',
'Atlanta Georgia',
'Stone Mountain Park',
'Coca-Cola Olympic Park',
'Big Chicken Marietta Georgia']

for destination in destinations:
	g = geocoder.arcgis(destination)
	my_list=g.latlng
	lat=my_list[0]
	lng=my_list[1]
	url=dark_sky + my_key + "/" + str(lat) + "," + str(lng)
	weather = requests.request('GET', url).json()
	for k, v in weather.items():
		if k == 'currently':
			forecast = weather[k]
			for key,value in forecast.items():
			    if key == 'temperature':
				temp = (forecast['temperature'])
                            if key == 'humidity':
                                hum = (forecast['humidity'])
			    if key == 'summary':
			        currently =(forecast['summary'])
                                print("{\"loc\":\"" + destination + "\",\"sysdate\":\"" + now.strftime("%Y-%m-%d %H:%M")+ "\"" + ',"temp\":\"' + str(temp)[0:4] + "\",\"hum\":\"" + str(hum)[0:4] + '\",\"forecast\":\"' + currently + '\"}')
                                file.write("{\"loc\":\"" + destination + "\",\"sysdate\":\"" + now.strftime("%Y-%m-%d %H:%M")+ "\"" + ',"temp\":\"' + str(temp)[0:4] + "\",\"hum\":\"" + str(hum)[0:4] + '\",\"forecast\":\"' + currently + '\"}')
                                file.write("\n")

file.close()
