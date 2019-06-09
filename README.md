# **Heatmap** (aka class_presentation)
**Desc**: Python solution to process IOT sensors and weather data

**Usage**: Unzip mqtt.zip to same directory as class_presentation.ipyb. You need 2 files to run the notebook, weather_collect.txt and mqtt.txt. Both of these files should be in the same directory as the jupyter notebook class_presentation.ipyb. From there, the notebook does all the work. If you are looking to **generate your own data**, the script **swat_temp_pub.py** runs on the Raspberry Pi, pulls temp and humidity, formats to JSON and streams to an MQTT server (which is currently in the cloud). **Weather_collect.py** scrapes the weather data. If you use these scripts, you will need to change a few settings to get it to work successfully for you, but the changes are remedial, just passwords and api-keys, mainly.

**Abstract**:
Concerned with utility costs incurred during summer peak months, this project aimed to explore ways to stabilize and reduce cooling costs inside residential homes. Before making any financial commitments to upgrade cooling equipment, we investigated ways to improve efficiencies. Lacking current information about the "domestic thermal qualities" or HVAC and insulation efficiencies, we set out to study the impact of the external environment on our home's a/c usage as well as to assess the current a/c unit’s cooling abilities. The challenge was to make reliable assessments within a budget. The first objective was to evaluate the a/c cooling unit's effectiveness. The second objective was to determine if the overall goal could be met economically, by making small changes indoors to promote cooling effeciency in a substantial way. 

**Methods**:
Raspberry Pi microcomputers were fitted with sensors to measure temperature and humidity and then stream the data to cloud. The sensors were a collection of DHT22 and DHT11 sensors, each recording temperature and humidity through the duration of the study. Separately, a weather polling service using python was scripted to record the weather information every 10 minutes, in 4 parts of the city, including the area where the residential study was conducted. 

**Results**: 
We found the temperature and humidity fluctuates widely from one part of the city to another, and that the humidity was negatively correlated with temperature. Concerning the indoors study, the temperature in the kitchen (M=77.3, S.D.=.75), the living room (M=77.1, SD=.83), the master bedroom (M=73.71, SD=.76) and the guest bedroom (M=79.3, SD=.60)) varied widely. A similar trend was observed with respect to humidity in the kitchen (M=47.1, SD=2.52), living room (M=48.9, SD=2.77), master bedroom (M=54.5, SD=2.02) and guest bedroom (M=46.4, SD=1.70). Aggregating across all 4 rooms, humidity was weakly negatively correlated with temperature. The highest temperatures were observed in a guestroom containing multiple electronic devices, including several computer servers, and this same room had a window facing the sun with minimal window covering. Given that the a/c control unit was attempting to achieve one stable temperature throughout the house, and that the coldest room was generally 2 degrees cooler than the remaining rooms, it appears that the ventilation system was overcooling 1 room in order to compensate for undercooling in the hottest room. On a positive note, the range of humidity values collected internally showed the a/c is effective in removing humidity (see heat index). As the temperature in the majority of rooms stayed at within a consistent range near the HVAC thermostat temperature setting, we see the a/c's ability to cool is acceptable..The correlation between weather and internal environment for temp was 4.6% and the humidity was even less at 3%. This confirms the effectiveness of the a/c cooling unit.

**Conclusions**:
A substantial HVAC expenditure is not needed at this time. Restricting the amount of direct sunlight on the hottest room, engaging a dehumidifier near the thermostat, and restricting the ventilation going to the coldest room, will likely balance the rates at which each room cools and reduce the amount of time the a/c is engaged and lead to substantial cost savings.

