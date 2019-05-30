# Heatmap
Desc: Python solution to process IOT sensors and weather data

Usage: Unzip mqtt.zip to same directory as class_presentation.ipyb. You need 2 files to run the notebook, weather_collect.txt and mqtt.txt. Both of these files should be in the same directory as the jupyter notebook class_presentation.ipyb. From there, the notebook does all the work.

Abstract:
Concerned with utility costs during summer peak months, ideas on how to reduce spending came up. Before making any big ticket commitments, we started looking at ways to improve utility efficiencies. We lacked current information about the "domestic thermal qualities" or HVAC and insulation efficiencies, so we set out to study the impact of the environment on our home's a/c usage as well as assess the a/c cooling abilities. 

Methods:
Raspberry Pi microcomputers were fitted with sensors to measure temperature and humidity and then stream the data to cloud. The sensors were a collection of DHT22 and DHT11 sensors, each collecting temperature and humidity. A weather polling service using python was scripted to collect the weather information in 4 parts of the city, including the area where the study was conducted. The sensors collected data each minute, while the weather poll collected every 10 minutes. 

Results: 
A week's worth of data was consumed using Panda. We found the weather fluctuates from one part of the city to another, and the humidity was negatively correlated to the temperature. Concerning indoors, the environmental elements in each room varied significantly and the humidity was weakly negatively correlated to the temperature. The hottest room we determined to be filled with electronics and had a window facing the sun - of which only minimal window covering was present. The coldest room was found to stay generally 2 degrees cooler than the remaining rooms. The ventilation system was overcooling 1 room, in order to manage the temperature in the hottest room. On a positive note, the range of humidity values collected internally showed the a/c is effective in removing humidity (see heat index). As the temperature in the majority of rooms stayed at within a consistent range near the HVAC thermostat temperature setting, we see the a/c's ability to cool is acceptable.

Conclusions:
A big ticket HVAC expenditure is not needed at this time. By restricting the amount of direct sunlight on the hottest room and restricting the ventilation going to the coldest room, we are hoping to balance the rates at which each room cools and reduce the amount of time the a/c is engaged.

