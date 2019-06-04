#!/usr/bin/env python
# coding: utf-8

# <a id='title'></a>
# # <bold><font color=gray>Jupyter App:</font><font color=darkpink> A Student's Analysis of his Domestic Thermal Footprint</font></bold>
# ## <bold><font color=white>=================</font><font color=purple>Or, how the Raspberry Pi saved me $5,000.</font>

# ## <font size=5 color=darkpink>Abstract:</font>
# 
# Concerned with utility costs incurred during summer peak months, this project aimed to explore ways to stabilize and reduce cooling costs inside residential homes. Before making any financial commitments to upgrade cooling equipment, we investigated ways to improve efficiencies.  Lacking current information about the "domestic thermal qualities" or HVAC and insulation efficiencies, we set out to study the impact of the external environment on our home's a/c usage as well as to assess current a/c unit’s cooling abilities. The challenge was to make reliable assessments within a budget. The first objective was to evaluate the a/c cooling unit's effectiveness. The second objective was to determine if the overall goal could be met economically, by making small changes indoors to promote cooling effeciency in a substantial way. <font color=darkpink>**Methods**:</font> Raspberry Pi microcomputers were fitted with sensors to measure temperature and humidity and then stream the data to cloud. The sensors were a collection of DHT22 and DHT11 sensors, each recording temperature and humidity through the duration of the study. Separately, a weather polling service using python was scripted to record the weather information every 10 minutes, in 4 parts of the city, including the area where the residential study was conducted. <font color=darkpink>**Results:**</font> We found the temperature and humidity fluctuates widely from one part of the city to another, and that the humidity was negatively correlated with temperature. Concerning the indoors study, the temperature in the kitchen (M=77.3, S.D.=.75), the living room (M=77.1, SD=.83), the master bedroom (M=73.71, SD=.76) and the guest bedroom (M=79.3, SD=.60))** varied widely. A similar trend was observed with respect to humidity in the kitchen (M=47.1, SD=2.52), living room (M=48.9, SD=2.77), master bedroom (M=54.5, SD=2.02) and guest bedroom (M=46.4, SD=1.70). **Aggregating across all 4 rooms, humidity was weakly negatively correlated with temperature**. The highest temperatures were observed in a guestroom containing multiple electronic devices, including several computer servers, and this same room had a window facing the sun with minimal window covering. Given that the a/c control unit was attempting to achieve one stable temperature throughout the house, and that the coldest room was generally 2 degrees cooler than the remaining rooms, it appears that the ventilation system was overcooling 1 room in order to compensate for undercooling in the hottest room. On a positive note, the range of humidity values collected internally showed the a/c is effective in removing humidity (see heat index). As the temperature in the majority of rooms stayed at within a consistent range near the HVAC thermostat temperature setting, we see the a/c's ability to cool is acceptable..**The correlation between weather and internal environment for temp was 4.6% and the humidity was even less at 3%.** This confirms the effectiveness of the a/c cooling unit. <font color=darkpink>**Conclusions:**</font> A substantial HVAC expenditure is not needed at this time. Restricting the amount of direct sunlight on the hottest room, engaging a dehumidifier near the thermostat, and restricting the ventilation going to the coldest room, will likely balance the rates at which each room cools and reduce the amount of time the a/c is engaged and lead to substatial cost savings.

# 
#     
# ## <font size=5 color=gray>Notebook Purpose: </font><font color=darkblue>Process and Present Data using Pandas </font><font color=darkblue> including:</font>
# <font color=white size=1>==========================================================================================================================================================================</font>
# <font size=2  color=gray>> using </font><font color=darkblue>**JSON, Lists, Dictionaries, Loops, Dictionary Writer, Z-scores with SciPy, Heat-Maps with Seaborn and Visualizing with MatPlotLib**</font>
# <font color=white size=1>==========================================================================================================================================================================</font>
# <font size=2  color=gray> via ugly colors and links.</font>
# <a href ='#top'>Jump to Table of Contents</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a> 
# 
# ### <a id='top'></a>
# <font color=black size=1>=============================================================================================================</font>
# ### <font size=5 color=darkpink>Table of Contents</font>
# <font color=black size=1>=============================================================================================================</font>
# 
# <a href='#methods'><font color=darkpink>**Methods**</font></a>
# 
# <a href='#section1'><font color=darkblue>**Section1:     Process Atlanta weather data**</font></a>
# 
# <a href='#sec1pt1'>Part 1 - Read in raw JSON, write out CSV spreadsheet</a>
# 
# <a href='#sec1pt2'>Part 2 - Review Weather MetaData</a>
# 
# <a href='#sec1pt3'>Part 3 - Data Edits - Format DATES</a>
# 
# <a href='#sec1pt4'>Part 4 - Breakout DataFrames by Location</a>
# 
# <a href='#sec1pt5'>Part 5 - Visualize Weather Data for Completeness</a>
# 
# <a href='#section2'><font color=darkblue>**Section2:     Process Home Environment (Internal Data)**</font></a>
# 
# <a href='#sec2pt1'>Part 1 - Read, write and remove dups from Environment Data CSV spreadsheet</a>
# 
# <a href='#sec2pt2'>Part 2 - Review Environment MetaData</a>
# 
# <a href='#sec2pt3'>Part 3 - Renaming Columns and Replacing Data</a>
# 
# <a href='#sec2pt4'>Part 4 - Visualize and Assess Environment Data</a>
# 
# <a href='#results'><font color=darkpink>**Results**</font></a>
# 
# <a href='#sec3pt1'>Part 1 - Present Weather findings</a>
# 
# <a href='#sec3pt2'>Part 2 - Present Environment findings</a>
# 
# <a href='#sec3pt3'>Part 3 - Present All Data together</a>
# 
# <a href='#conclusions'><font color=darkpink>**Conclusions**</font></a>
# 
# <a href='#section4'><font color=darkblue>**Section1:    Comparative Analysis**</font></a>
# 
# <a href='#sec4pt2'><font color=darkblue>**Section2:     Conclusions**</font></a>
# 
# <a href='#sec4pt3'><font color=darkblue>**Section3:     Limitations and Future Plans**</font></a>

# In[60]:


# Set the my_dir to a path you want to save figures in this notebook.
# if you do not want to save images, simply set my_dir to blanks
# example: my_dir ='' (you just uncomment out this line...)
import os
my_dir = 'C:/users/bucbo_000/desktop/python/images'
#my_dir=''
if os.path.exists(my_dir):
    if os.path.isdir(my_dir):
        os.chdir(my_dir)
else:
    my_dir = ''


# <a id='methods'></a>
# <font color=black size=1>=============================================================================================================</font>
# 
# 
# <font color=darkpink size=10>Methods</font>
# 
# <font color=black size=1>=============================================================================================================</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# <font color=black>This project is part of an larger, ongoing IOT project. In particular, where the sensors could be monitoring a warehouse to assist in environmental controls. 
#     
# **Initial development**
# 
# The home was chosen a location for proof of concept, with zero cost and complete control over location. The idea was to complete P.O.C. and then build to incorporate additional robust sophistication when implementing in larger or more complex locations where the environment needs managing. Sensors more accurate than the ones we chose were considered cost prohibitive and overly complex for a P.O.C using ARM microcomputers (the Raspberry PI). Eventually this proof of concept functionality will be absorbed by the larger, ongoing IOT project.
# 
# 
# <font size=10 color=white></font>
# **Locations**
# 
# Testing in a home was the most viable location, in terms of cost and usage. At the time of this project, acquiring access to a warehouse remained pending and considered out of reach. Other IOT projects that tied into the larger IOT project were tested and demonstrated in an office complex presentation room. This too, was considered to be out of reach. Concerning the weather, 4 parts of Atlanta were tracked, The north side of the perimeter, Marietta (west), Stone Mountain (east) and downtown at the Coca-Cola Olympic Village (south). The rational was taking a radius between the home and the downtown Capital and extending east and west. Latitude and Longitude were captured as well as weather information, for later use in visualizing the location (if desired), allowing for exact determination of where the weather was being extracted. 
# 
# **Measures**
# 
# The sensors were not calibrated. Upon initial activation of the sensor, the data captured was compared to a true thermostat. Any sensor reporting temperature measurements beyond 5 celsius were discarded and replaced. We found a high correspondence between the accuracy of reported temp and the accuracy of reported humidity. Restating, we found when a sensor reported an unacceptable temperature, we found the humidity was also highly skewed. Take note, the DHT22 sensor, which is more accurate than the DHT11 sensor, requires a 10K resistor to keep the microcomputer port current from impacting the reported signal - the reported temp and humidity. The additional cost was less than .01 (actual cost is 2.00 - as buying resistors in bulk is cheaper than purchasing individually).
# 
# <img src="mqtt-pandas.png" width=1000, height=200>
# <img src="image.png">
# 
# **Hardware Specifics** compliments of https://www.mouser.com/ds/2/737/dht-932870.pdf and https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/
# 
# 

# # <a id='section1'></a>
# # <font color=darkpink>Section 1: Process Atlanta Weather Data</font>
# <a href ='#top'>Jump to Table of Contents</a>

# <a id='sec1pt1'></a>
# ## <font color=darkblue>Part 1 - Read in raw JSON, write out CSV spreadsheet</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Edit check for valid JSON format.</font>
# </div>

# In[2]:


import csv as csv
import json
from pandas.io.json import json_normalize
import matplotlib
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
from scipy import stats
from matplotlib import style
#------------------------------------------------#
# Set processing parameters and directives
#------------------------------------------------#
#matplotlib.use('nbagg')
style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (16,12)
plt.rcParams['font.size'] = 8
#------------------------------------------------#
# Set the appropriate path
#------------------------------------------------#
home_path = 'C:\\users\\bucbo_000\\Desktop'

if os.path.isdir(home_path):
    os.chdir(home_path)
else:
    home_path='./'


#------------------------------------------------#
#Open files for JSON read and write LIST
#------------------------------------------------#
data_file = open('weather_collect.txt', "r", encoding = 'utf-8')     

#-------------------------------------------------#
# Convert json to list of dictionaries, then parse accordingly
# IF JSON is INVALID - the json.loads will error. We
# trap the error and simply move onto the next record.
#-------------------------------------------------#

f1 = data_file.readlines()
my_df = list()
for x in f1:
    try:
        data = json.loads(x) 
        df = data
        my_df.append(df)
    except:
        print("skipping: JSON format invalid for:", x)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Write valid data to list of dictionaries for consumption by dictionary writer, a child class of cvs module.</font>
# </div>
# 

# In[3]:


#------------------------------------------------#
# Define output file and header line
#------------------------------------------------#
with open('weather.csv', 'w', newline='') as csvfile:
    fieldnames = ['sysdate', 'loc', 'temp', 'hum','forecast', 'lat', 'lon']
# This opens the `DictWriter`.
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
# Write out the header row (this only needs to be done once!).
    writer.writeheader()
#------------------------------------------------#
# Read in, Write out and Loop 
#------------------------------------------------#
    for a_df in my_df:
        try:
            writer.writerow(a_df)
        except:
            print("Unable to parse, skipping record...")


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Build DataFrame from list of dictionaries.</font>
# </div>

# In[4]:


ext_df = pd.read_csv(home_path + "\\weather.csv", usecols=range(0,5)) 


# In[5]:


plt.rcParams['figure.figsize'] = (20,15)
plt.rcParams['font.size'] = 15

a = ext_df.groupby(['loc', 'forecast'])['temp'].mean().unstack().dropna(axis = 0)
x = list(a)
x


slices = [8,8,8,8,8,8,8,8,8,8,8,8,8,8]
activities = x
cols=['m','g','y','b','r','k','pink']

plt.pie(slices, labels=activities
        , startangle=90
        , colors=cols
        , shadow=True
        , explode=(0, 0,0,0,0,0,0,0,0,0,0,0.2,0,0)
#        , autopct = '%1.1f%%'
       )
plt.title('Weather\nExploratory Investigation\nReview Metadata')

if my_dir:
    plt.savefig(my_dir + '/' + 'Review_Exploratory_Metadata.png')


# <a id='sec1pt2'></a>
# ### <font color=darkblue>Part 2 - Review Weather MetaData.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Visualize Metadata and look for holes in data.</font>
# </div>
#     
# <font size=3 color=blue>Figure 1a. Displays the raw weather metadata collected to identify if data is missing.</font>

# In[6]:


#----------------------------------------#
# This WILL NOT RUN with NaN records, so...
#    using dropna() function to strip all 
#    records that have nulls in them. 
# This assessment is based on this data, 
#    and should not be considered a best
#    practice.
#----------------------------------------#
for col in ext_df.columns:
    plot_data = ext_df[col].dropna()
    fig, ax = plt.subplots()
    ax.plot(plot_data.values,plot_data.index.values,  label=col)

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_1a_review_weather_metadata_raw.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Show DataFrame sample.</font>
# </div>
# 
#     
# <font size=3 color=blue>Table 1a. displays a random sampling of the weather data collected</font>

# In[7]:


ext_df.sample(n=10)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>:  Review summary of weather data collected.</font>
# </div>
#     
# <font size=3 color=blue>Table 1b. Summarizes the mean temperature and humidity  by location and forecast</font>

# In[8]:


x = ext_df.groupby(['forecast', 'loc'])['temp', 'hum'].mean().unstack().fillna('-')
x


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 4</b> </font><font color=darkblue>: Review raw data Heat Map.</font>
# </div>
#     
# <font size=3 color=blue>Figure 1b. Summarizes the raw data as a Heat Map to supplement Table 1b results.</font>
# 
# <font size=3 color=purple>Notice that Coca-Cola Olympic Village has the highest diversity in forecasts.</font>

# In[9]:


corr =  ext_df.groupby(['forecast', 'loc'])['temp'].mean().unstack()
ax = sns.heatmap(
    corr, 
    
    cmap=sns.diverging_palette(10, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_1b_heatmap_atlanta_weather.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 5</b> </font><font color=darkblue>: Review content metadata stats.</font>
# </div>
# 
# <font size=3 color=blue>Table 1d. displays the weather ***metadata*** statistics</font>

# In[10]:


print("------------------------------------")
print("Weather Data has ", ext_df.shape[0], "Rows and", ext_df.shape[1], "Columns of types:")
print("------------------------------------")
print(ext_df.dtypes)
print(" ")
print("------------------------------------")
print(f"Weather Data nulls search:")
print("------------------------------------")
print(ext_df.isnull().sum())
print(" ")
print()
print("------------------------------------")
print(f"Weather Data counts (raw)")
print("------------------------------------")
for i in ext_df.columns:
    print("The count for", i, "is", ext_df[i].count())
print(" ")
print("------------------------------------")
print(f"Weather Data counts excluding nulls:")
print("------------------------------------")
print(ext_df.dropna().count())
print(" ")
print("------------------------------------")
print(f"Weather Data statistics:")
print("------------------------------------")
ext_df.describe([0])


# <font size=1 color=black>===============================================================================================================</font>
# ## <font color=darkpink>Clean the weather data.</font>
# <font size=1 color=black>===============================================================================================================</font>

# ### <font color=red>Discrepancy!</font><font color=darkgray> The </font><font color=darkorange>weather</font><font color=darkgray> humidity is in </font><font color=darkorange> percentages</font><font color=darkgray> while the </font><font color=blue> indoors </font><font color=darkgray> humidity is in </font><font color=blue>integers</font>

# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 6</b> </font><font color=darkblue>: Convert the humidity before moving on.</font>
# </div>

# In[11]:


ext_df['hum'] = (ext_df['hum'] * 100)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 7</b> </font><font color=darkblue>: Drop null weather data.</font>
# </div>

# In[12]:


ext_df.dropna(axis=0, inplace=True)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 8</b> </font><font color=darkblue>: Take sample and verify results.</font>
# </div>
# 
# <font size=3 color=blue>Table 1e. Shows a sample of the cleaned weather ***data*** </font>

# In[13]:


ext_df.sample(n=5)


# <a id='sec1pt3'></a>
# ## <font color=darkblue>Part 3 - Format DATES and build indicies.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Format the sysdate column to be a pandas DATE object.</font></div>

# In[14]:


ext_df['sysdate'] = pd.to_datetime(ext_df['sysdate'])


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Validate the DATE conversion worked.</font></div>
# 
# <font size=3 color=blue>Table 1f. Shows the data types of columns - to validate sysdate is now a datetime object </font>

# In[15]:


ext_df.dtypes


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Build index for visualization preparation.</font></div>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# In[16]:


ext_df.set_index(['sysdate'], inplace=True)
ext_df.sort_index(inplace=True)


# <a id='sec1pt4'></a>
# ## <font color=darkblue>Part 4 - Breakout DataFrames by Location.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Create new dataframes by location in city.</font></div>

# In[17]:


ext_atl = ext_df[ext_df['loc'] == 'Atlanta Georgia']
ext_marietta = ext_df[ext_df['loc'] == 'Big Chicken Marietta Georgia']
ext_stonemtn = ext_df[ext_df['loc'] == 'Stone Mountain Park']
ext_coke = ext_df[ext_df['loc'] == 'Coca-Cola Olympic Park']


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Take sub-group sample stat to ensure dataframes built correctly.</font></div>
# 
# <font size=3 color=blue>Table 1g. Shows a breakout of forecasts.</font>

# In[18]:


ext_atl['forecast'].value_counts()


# <a id='sec1pt5'></a>
# ## <font color=darkblue>Part 5 - Visualize External Data for Completeness.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Breakout external data by groups.</font></div>

# In[19]:


ext_df.drop(columns = ['forecast']).groupby(['loc']).count()


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Merge external data groups.</font></div>

# In[20]:


ow = ext_atl.join(ext_marietta, how='left', lsuffix='_atl', rsuffix='_marietta')
sw = ext_coke.join(ext_stonemtn, how='left', lsuffix='_coke', rsuffix='_stnmtn')
outside = ow.join(sw, how='left')
outside.sort_index(inplace=True)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Do basic plot as a test.</font></div>
# 
# ### <font color = blue size=3>Figure 1b - Initial display of weather temp and humidity</font>
# 
#  <font color=purple size=3> This actually discloses a lot, but we avoid details, as we stay on track of presentation.</font>

# In[21]:


outside.plot(figsize=(22,11))
plt.xlabel('Dates', color='green')
plt.ylabel('Temperature and Humidity', color='red')
plt.title('External Weather Raw Data\n--------\nTemperature and Humidity', color='blue')

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_1b_weather_temp_hum_raw_data.png')


# 
# ### <font color = blue size=3>Figure 1c - Same data as figure 1b, but smoothed with rolling mean</font>

# In[22]:


ext_df['avg_temp'] = ext_atl['temp'].rolling(10).mean().dropna()
ext_df['avg_hum'] = ext_atl['hum'].rolling(10).mean().dropna()
ax = ext_df['avg_hum'].plot()
ax1 = ext_df['avg_temp'].plot(ax = ax, figsize=(22,11))
plt.xlabel('Dates', color='green')
plt.ylabel('Temperature and Humidity', color='red')
plt.title("Derived Mean of External Temperature and Humidity\nSmoothed by Rolling Mean of 10 samples", color='blue')
plt.legend()
if my_dir:
    plt.savefig(my_dir + '/' + 'fig_1c_weather_temp_hum_raw_data.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 4</b> </font><font color=darkblue>: Present external temperatures.</font></div>
# 
# ### <font color = blue size=3>Figure 1d - Initial display of weather temp</font>

# In[23]:


outside.drop(columns=['hum_atl', 'hum_coke','hum_stnmtn', 'hum_marietta']).plot(figsize=(22,11))
plt.xlabel('Dates', color='green')
plt.ylabel('Temperature', color='red')
plt.title('Composite of Temperature Data collected from Weather Service', color='blue')

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_1d_weather_temp.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 5</b> </font><font color=darkblue>: Present external humidities.</font></div>
# 
# ### <font color = blue size=3>Figure 1e - Initial display of weather humidity</font>

# In[24]:


outside.drop(columns=['temp_atl', 'temp_coke','temp_stnmtn', 'temp_marietta']).plot(figsize=(22,11))
plt.xlabel('Dates', color='green')
plt.ylabel('Humidity', color='red')
plt.title('Composite of Humidity Data collected from Weather Service', color='blue')

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_1e_weather_humidity.png')


# <a id='section2'></a>
# # <font color=darkpink>Section 2: Process Home Environment(Indoor Data)</font>
# <a href ='#top'>Jump to Table of Contents</a>
# 

# ### <a id='sec2pt1'></a>
# ## <font color=darkblue>Part 1 - Read, write and remove dups from environment data csv spreadsheet</font>
# 
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Edit and Build step combined - See Section 1 for step by step details.</font></div>
# 
# ### <font color = blue size=3>Table 2a - Shows indoor data that was cleaned off or rejected</font>

# In[25]:


import csv as csv
import datetime
import json
from pandas.io.json import json_normalize
import matplotlib
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

# Set the appropriate path

#------------------------------------------------#
# Set processing parameters and directives
#------------------------------------------------#
matplotlib.use('nbagg')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (16,12)
plt.rcParams['font.size'] = 8
#------------------------------------------------#
# Set the appropriate path
#------------------------------------------------#


home_path = 'C:\\users\\bucbo_000\\Desktop'

if os.path.isdir(home_path):
    os.chdir(home_path)
else:
    home_path='./'
    
#Open files for read and write - write headings first
data_file = open('mqtt.txt', "r", encoding = 'utf-8')     

# Convert json to list of dictionaries, then parse accordingly

f1 = data_file.readlines()
my_df = list()
for x in iter(f1):
    try:
        data = json.loads(x)
        df = data #json_normalize(data)
        my_df.append(df)
    except:
        print("skipping: JSON format invalid for:", x)
        
cnt_accept = 0
cnt_reject =0
content_df = list()
for i in enumerate(my_df):
     for k,v in enumerate(i):
        #print(i)
        #print("v=", v)
        #if str(v).startswith('{\'device') and "loc" in str(v):
        if "env" not in str(i):
            content_df.append(my_df)
            cnt_accept +=1
        else:
            print("skipping: JSON content invalid")
            cnt_reject +=1
            
print("We now have", cnt_accept, "records to use after cleaning",cnt_reject, "rows")

cnt_accept = 0
cnt_reject = 0

# Define output file and header line
with open('mqtt.csv', 'w', newline='') as csvfile:
    fieldnames = ['device','sysdate', 'temp', 'hum', 'state']
# This opens the `DictWriter`.
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
# Write out the header row (this only needs to be done once!).
    writer.writeheader()
#
# Read in, Write out and Loop 
#
    for a_df in my_df:
        try:
            writer.writerow(a_df)
            cnt_accept += 1
        except:
            print("Unable to parse, skipping...")
            cnt_reject += 1

print("We now have", cnt_accept, "Dictionary records to use after cleaning",cnt_reject, "rows")


int_df = pd.read_csv(home_path + "\\mqtt.csv", usecols=range(0,4)) 

#######################################################
#
int_df = int_df.drop_duplicates()
#
#######################################################

int_df['sysdate'] = pd.to_datetime(int_df['sysdate'])


# <a id='sec2pt2'></a>
# ## <font color=darkblue>Part 2 - Review Environment Metadata</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Visualize Metadata and look for holes in data.</font>
# </div>
# 
#     
# <font size=3 color=blue>Figure 2a. Displays the raw indoor metadata collected to identify if data is missing.</font>

# In[26]:


for col in int_df.columns:
    plot_data = int_df[col].dropna()
    fig, ax = plt.subplots()
    ax.plot(plot_data.index.values, plot_data.values, label=col)
    plt.ylabel(col)
    plt.title("MetaData Dump\nfor review of missing data")

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_2a_indoor_raw_metadata_visual.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Review raw Metadata statistics.</font>
# </div>

# In[27]:


print("------------------------------------")
print("Environment Data has ", int_df.shape[0], "Rows and", int_df.shape[1], "Columns of types:")
print("------------------------------------")
print(int_df.dtypes)
print(" ")
print("------------------------------------")
print(f"Environment Data nulls search:")
print("------------------------------------")
print(int_df.isnull().sum())
print(" ")
print("------------------------------------")
print(f"Environment Data counts (raw)")
print("------------------------------------")
for i in int_df.columns:
    print("The count for", i, "is", int_df[i].count())
print("------------------------------------")
print(f"Environment Data counts:")
print("------------------------------------")
print(int_df.dropna().count())
print(" ")
print("------------------------------------")
print(f"Environment Data statistics:")
print("------------------------------------")
int_df.describe()
print(f"device cardinality:", int_df['device'].value_counts())
print(f"temp mean:", int_df['temp'].value_counts().mean())
print(f"humidity mean:", int_df['hum'].value_counts().mean())


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Review indoor temp for outliers.</font>
# </div>
# 
# ### <font color = blue size=3>Figure 2b - Initial display of indoor temp</font>

# In[28]:


int_df['temp'].plot(color='lightblue')
new_df = int_df.copy()
plt.xlabel('Dates', color='green')
plt.ylabel('Temperature', color='red')
plt.title('Indoor Temperature Raw Data', color='blue')
plt.legend()

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_2b_indoor_temp_raw.png')


# ### <font color = blue size=3>Figure 2c - Same data as Figure 2b - but presented using rolling mean</font>

# In[29]:


int_df['temp'].rolling(10).mean().plot(color='lightblue')
new_df = int_df.copy()
plt.xlabel('Dates', color='green')
plt.ylabel('Temperature', color='red')
plt.title('Indoor Temperature Raw Data\nSmoothed using Rolling Mean of 10 samples', color='blue')
plt.legend()

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_2c_indoor_temp_raw.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 4</b> </font><font color=darkblue>: Review summary of indoor data collected.</font>
# </div>
#     
# <font size=3 color=blue>Table 2b. Displays the temperature and humidity  by room.</font>

# In[30]:


import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (16,12)
plt.rcParams['font.size'] = 18

x = int_df.replace({'device': {'B8:27:EB:76:5F:45': 'Living Room', 'B8:27:EB:2D:40:28': 'Master Bedroom', 'B8:27:EB:37:B0:F8': 'Guest Bedroom', 'B8:27:EB:A9:D4:C2': 'Kitchen', 'DC:0:D30:48:FE:9C':'Master Bedroom'}}).groupby(['temp', 'device'])['hum'].min().unstack().fillna('-')
y = int_df.replace({'device': {'B8:27:EB:76:5F:45': 'Living Room', 'B8:27:EB:2D:40:28': 'Master Bedroom', 'B8:27:EB:37:B0:F8': 'Guest Bedroom', 'B8:27:EB:A9:D4:C2': 'Kitchen', 'DC:0:D30:48:FE:9C':'Master Bedroom'}}).groupby(['temp', 'device'])['hum'].max().unstack().fillna('-')
x  = x.join(y, how='left', lsuffix="_min", rsuffix='_max')
print(x)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 5</b> </font><font color=darkblue>: Clean up outliers.</font>
# </div>
# 
# ## <font color=blue>Notice</font><font color=purple> the wide swing in </font><font color=red>temp </font><font color=purple> ranges. Let's use Z-Score and clean up the temp outliers.

# In[31]:


print(abs(stats.zscore(int_df['temp'])).min())
print(abs(stats.zscore(int_df['temp'])).mean())
print(abs(stats.zscore(int_df['temp'])).std())
print(abs(stats.zscore(int_df['temp'])).max())
int_df = int_df[abs(stats.zscore(int_df['temp'])) < 2.0]


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 6</b> </font><font color=darkblue>: Review new data.</font>
# </div>
# 
# <font size=3 color=blue>Table 2c. Displays the temperature and humidity statistics.</font>

# In[32]:


print("------------------------------------")
print("Environment Data statistics:")
print("------------------------------------")
int_df.describe()


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 7</b> </font><font color=darkblue>: Clean up outliers.</font>
# </div>
# 
# ## <font color=blue>Notice</font><font color=purple> the wide swing in </font><font color=red>hum </font><font color=purple> ranges. Let's use Z-Score and clean up the hum outliers.

# In[33]:


print(abs(stats.zscore(int_df['hum'])).min())
print(abs(stats.zscore(int_df['hum'])).mean())
print(abs(stats.zscore(int_df['hum'])).std())
print(abs(stats.zscore(int_df['hum'])).max())
int_df = int_df[abs(stats.zscore(int_df['hum'])) < 2.0 ]


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 8</b> </font><font color=darkblue>: Review new data.</font>
# </div>
# 
# <font size=3 color=blue>Table 2d. Displays the **cleaned** temperature and humidity statistics.</font>

# In[34]:


print("------------------------------------")
print("Environment Data statistics:")
print("------------------------------------")
int_df.describe()


# <a id='sec2pt3'></a>
# ## <font color=darkblue>Part 3 - Rename columns, replace data and build index.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Change devices to match room location.</font>
# </div>

# In[35]:


int_df.replace({'device': {'B8:27:EB:76:5F:45': 'Living Room', 'B8:27:EB:2D:40:28': 'Master Bedroom', 'B8:27:EB:37:B0:F8': 'Guest Bedroom', 'B8:27:EB:A9:D4:C2': 'Kitchen', 'DC:0:D30:48:FE:9C':'Master Bedroom'}}, inplace=True)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: COLUMN renaming step to make columns meaningful.</font>
# </div>

# In[36]:


#int_df.rename(columns={'state': 'forecast'},inplace=True)
int_df.rename(columns={'device': 'room'}, inplace=True)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Set sysdate as index for internal data.</font>
# </div>

# In[37]:


int_df.set_index(['sysdate'], inplace=True)
int_df.sort_index(inplace=True)


# <a id='sec2pt4'></a>
# ## <font color=darkblue>Part 4 - Breakout DataFrames by location.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Create new dataframes by device or internal location.</font>
# </div>
# 
# ### <font color=purple>As this is taken during the summer, we can assume any temp below 70 F is to be removed.</font>

# In[38]:


mb = int_df[int_df['room'] == 'Master Bedroom']
lr = int_df[int_df['room'] == 'Living Room']
gb = int_df[int_df['room'] == 'Guest Bedroom']
kt = int_df[int_df['room'] == 'Kitchen']
#---------------------------------------------#
# Deprecated with Z-scoring above
#---------------------------------------------#
#mb = mb[mb['temp'] > 69]
#mb = mb[mb['temp'] < 90]
#lr = lr[lr['temp'] > 69]
#lr = lr[lr['temp'] < 90]
#gb = gb[gb['temp'] > 69]
#gb = gb[gb['temp'] < 90]
#kt = kt[kt['temp'] > 69]
#kt = kt[kt['temp'] < 90]


# <a id='sec2pt5'></a>
# ## <font color=darkblue>Part 5 - Visualize and Assess Environment Data.</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Display data counts by device.</font>
# </div>
# 
# <font size=3 color=blue>Table 2e. Displays the temperature and humidity counts by room</font>
# 
# <font size=3 color=blue>Table 2f. Displays the temperature and humidity mean by room</font>

# In[39]:


int_df.groupby(['room']).count()


# In[40]:


int_df.groupby(['room']).mean()


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Visualize the internal data's metadata.</font>
# </div>
#     
# ### <font color = blue size=3>Figure 2c - Review environment metadata to assess if missing we are missing data.</font>

# In[ ]:





# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Merge internal data groups.</font>
# </div>

# In[41]:


br = mb.join(gb, how='left',  lsuffix='_mstr', rsuffix='_guest')
lk = lr.join(kt, how='left', lsuffix='_living', rsuffix='_kit')
inside = br.join(lk, how='left')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 4</b> </font><font color=darkblue>: Visualize internal data.</font>
# </div>
# 
# ### <font color = blue size=3>Table 2d - Cleaner environment temp with humidity</font>

# In[42]:


inside.plot()
plt.xlabel('Dates', color='green')
plt.ylabel('Temperature and Humidity', color='red')
plt.title('Cooked (not-raw) Indoor Data\nComposite of indoor temperature and humidity', color='blue')

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_2d_indoor_data_cleaner.png')


# <a id='results'></a>
# <font color=black size=1>=============================================================================================================</font>
# 
# 
# <font color=darkpink size=10>Results</font>
# 
# <font color=black size=1>=============================================================================================================</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# A total of 4 sensors were used to tally the indoors environment. The kitchen (kt) and mstr bedroom (mb) sensors are using a DHT11 - so they're the least sensitive of all the other DHT-22 sensors. The sensors took reading every minute, provided the device was running properly. Starting May 24, 2019 **the thermostat stayed fixed at 76 F, as a control**. After the first week, a humidifier was engaged in the living room and the thermostat was set to**78 F and remained there for the duration of the study** (till June 6th, 2019)
# 
# **Identification of Items**
# The kitchen and master bedroom both have direct plumbing in them, which would lean towards having a higher room humidity count than rooms without plumbing. Unexplainably, the living room had a higher humidity count than did the kitchen. Both kitchen and masterbath were checked for leaks and none were found. Further research is needed to explain why the living room consistently had a higher humidity rate than the kitchen.

# <a id='sec3pt1'></a>
# ## <font color=darkblue>Part 1 - Present Weather Findings</font>
# 
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Present humidity corresponding to temp.</font>
# </div>
# 
#     
# ### <font color = blue size=3>Figure 3a - Display of Weather correlating Humidity to Temperature.</font>

# In[43]:


fs=22
ax = ext_atl.plot(kind="scatter", x='hum', y="temp",label="ATL", c='b')
ax2 = ext_marietta.plot(kind="scatter", x='hum', y="temp",label="MAR", c='orange', ax = ax)
ax3 = ext_coke.plot(kind="scatter", x='hum', y="temp",label="COKE", c='r' , ax = ax)
ax4 = ext_stonemtn.plot(kind="scatter", x='hum', y="temp",label="STNMNT", c='brown' , ax = ax)
plt.xlabel('Humidity', color = 'green', fontsize=fs)
plt.ylabel('Temperature', color='red', fontsize=fs)
plt.title('Display of Outdoor Weather\nTemperature and Humidity', color='blue', fontsize=fs)

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_3a_weather_correlate_temp_hum.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Review the temp - highs and lows.</font>
# </div>
# 
# ### <font color = blue size=3>Table 3a - Display cleaned weather temp with humidity highs and lows.</font>

# In[44]:


a = ext_df[['loc', 'temp']].groupby('loc').max().sort_values('temp', ascending=False)
b = ext_df[['loc', 'temp']].groupby('loc').min().sort_values('temp', ascending=True)
a.join(b,  lsuffix='_high', rsuffix='_low')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Review the temp - highs and lows.</font>
# </div>
# 
# ### <font color = blue size=3>Table 3b - Display cleaned outdoors temp statistics.</font>

# In[45]:


ext_df.groupby('loc')['temp'].describe()


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 4</b> </font><font color=darkblue>: Show the weather elements standard deviations between parts of city.</font>
# </div>

# In[46]:


print("######################################")
print("#Weather Standard Deviations between parts of the city.")
print("######################################")
print("# Keys: ext_atl      General ATL weather ")
print("#       ext_coke     Coca-Cola Olypmic Village")
print("#       ext_marietta KFC 40' chicken in Marietta")
print("#       ext_stonemtn Stone Mountain Park, Stone Mtn., Ga.")
print("#")
print('# ext_atl      temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(ext_atl['temp'].std(), ext_atl['hum'].std()))
print('# ext_coke     temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(ext_coke['temp'].std(), ext_coke['hum'].std()))
print('# ext_marietta temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(ext_marietta['temp'].std(), ext_marietta['hum'].std()))
print('# ext_stonemtn temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(ext_stonemtn['temp'].std(), ext_stonemtn['hum'].std()))


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 5</b> </font><font color=darkblue>: Show the Weather correlation between parts of city.</font>
# </div>

# In[47]:


print("######################################")
print("# External Environment Correlation Information.")
print("######################################")
print("# Keys: ext_atl      General ATL weather ")
print("#       ext_coke     Coca-Cola Olypmic Village")
print("#       ext_marietta KFC 40' chicken in Marietta")
print("#       ext_stonemtn Stone Mountain Park, Stone Mtn., Ga.")
print("#")
print('# Correlate ext_atl to ext_coke     Temperature:{0:4.1f}%'.format(ext_atl.corrwith(ext_coke)[0] * 100))
print('#                                   Humidity:{0:4.1f}%'.format(ext_atl.corrwith(ext_coke)[1] * 100))
print("#")
print('# Correlate ext_atl to ext_marietta Temperature:{0:4.1f}%'.format(ext_atl.corrwith(ext_marietta)[0] * 100))
print('#                                   Humidity:{0:4.1f}%'.format(ext_atl.corrwith(ext_marietta)[1] * 100))
print("#")
print('# Correlate ext_atl to ext_stonemtn Temperature:{0:4.1f}%'.format(ext_atl.corrwith(ext_stonemtn)[0] * 100))
print('#                                   Humidity:{0:4.1f}%'.format(ext_atl.corrwith(ext_stonemtn)[1] * 100))
print("#")


# <a id='sec3pt2'></a>
# ## <font color=darkblue>Part 2 - Present Environment findings</font>
# 
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Present humidity corresponding to temp.</font>
# </div>
# 
#     
# ### <font color = blue size=3>Figure 3b - Display of Environment correlating Humidity to Temperature.</font>

# In[48]:


fs=22
ax = mb.plot(kind="scatter", x='hum', y="temp",label="MSTR", c='b')
ax2 = lr.plot(kind="scatter", x='hum', y="temp",label="LIVING", c='orange', ax = ax)
ax3 = gb.plot(kind="scatter", x='hum', y="temp",label="GUEST", c='r' , ax = ax)
ax4 = kt.plot(kind="scatter", x='hum', y="temp",label="KITCHEN", c='brown' , ax = ax)
plt.xlabel('Humidity', color='green', fontsize=fs)
plt.ylabel('Temperature', color='red', fontsize=fs)
plt.title('Scatter plot of Indoor Data\nCorrelating Humidity to Temperature', color='blue', fontsize=fs)
if my_dir:
    plt.savefig(my_dir + '/' + 'fig_3b_indoors_correlate_temp_hum.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Review the data - highs and lows.</font>
# </div>
# 
# ### <font color = blue size=3>Table 3c - Display outdoors temp highs and lows.</font>

# In[49]:


a = int_df[['room', 'temp']].groupby('room').max().sort_values('temp', ascending=False)
b = int_df[['room', 'temp']].groupby('room').min().sort_values('temp', ascending=True)
a.join(b,  lsuffix='_high', rsuffix='_low')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 3</b> </font><font color=darkblue>: Show the environment elements standard deviations between parts of home.</font>
# </div>

# In[50]:


print("######################################")
print("#Environment Standard Deviations between parts of the home.")
print("######################################")
print("# Keys: kt           Kitchen - nearest thermostat ")
print("#       lr           Living Room")
print("#       mb           Master Bed")
print("#       gb           Guest Bed")
print("#")
print('# kt      temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(kt['temp'].std(), kt['hum'].std()))
print('# lr      temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(lr['temp'].std(), lr['hum'].std()))
print('# mb      temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(mb['temp'].std(), mb['hum'].std()))
print('# gb      temp & hum standard deviation: {0:4.2f} \t{1:4.2f}'.format(gb['temp'].std(), gb['hum'].std()))


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 4</b> </font><font color=darkblue>: Show the environment correlations between parts of home.</font>
# </div>

# In[51]:


print("######################################")
print("#Environment Correlations between parts of the home.")
print("######################################")
print("# Keys: kt           Kitchen - nearest thermostat ")
print("#       lr           Living Room")
print("#       mb           Master Bed")
print("#       gb           Guest Bed")
print("#")
print('# Correlate kt to lr     Temperature:{0:4.1f}%'.format(kt.corrwith(lr)[0] * 100))
print('#                           Humidity:{0:4.1f}%'.format(kt.corrwith(lr)[1] * 100))
print("#")
print('# Correlate kt to mb      Temperature:{0:4.1f}%'.format(kt.corrwith(mb)[0] * 100))
print('#                            Humidity:{0:4.1f}%'.format(kt.corrwith(mb)[1] * 100))
print("#")
print('# Correlate kt to gb      Temperature:{0:4.1f}%'.format(kt.corrwith(gb)[0] * 100))
print('#                            Humidity:{0:4.1f}%'.format(kt.corrwith(gb)[1] * 100))
print("#")
print('# Correlate mb to gb      Temperature:{0:4.1f}%'.format(mb.corrwith(gb)[0] * 100))
print('#                            Humidity:{0:4.1f}%'.format(mb.corrwith(gb)[1] * 100))
print("#")
print('# Correlate mb to lr      Temperature:{0:4.1f}%'.format(mb.corrwith(lr)[0] * 100))
print('#                            Humidity:{0:4.1f}%'.format(mb.corrwith(lr)[1] * 100))
print("#")
print('# Correlate gb to lr      Temperature:{0:4.1f}%'.format(gb.corrwith(lr)[0] * 100))
print('#                            Humidity:{0:4.1f}%'.format(gb.corrwith(lr)[1] * 100))


# <a id='sec3pt3'></a>
# ## <font color=darkblue>Part 3 - Present All Data together</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Review all cleaned data, side by side.</font>
# </div>
# 
# ### <font color = blue size=3>Figure 3c - Display the Outdoor and Indoor Data.</font>

# In[52]:


import numpy as np
fs=22
fig = plt.figure()
fig.patch.set_facecolor('lightgray')
fig.patch.set_edgecolor('orange')
graph1 = fig.add_subplot(2, 2, 1, facecolor='lightyellow')
graph1.plot(ext_df["temp"].rolling(10).mean(), ext_df['hum'].rolling(10).mean(), color='blue')
graph1.scatter(ext_df["temp"].rolling(10).mean(), ext_df['hum'].rolling(10).mean(), color='red')
graph1.set_title("Outdoor Weather\nTemperature and Humidity", color='blue')
graph1.set_xlabel('Temperature', color='green', fontsize=fs)
graph1.set_ylabel('Humidity', color='red', fontsize=fs)
graph1.set_xticks(np.arange(60, 100, step=10))
graph1.set_yticks(np.arange(0, 100, step=10))
graph2 = fig.add_subplot(2, 2, 2, facecolor='lightyellow')
graph2.plot(int_df["temp"].rolling(10).mean(), int_df['hum'].rolling(10).mean(), color='blue')
graph2.scatter(int_df["temp"].rolling(10).mean(), int_df['hum'].rolling(10).mean(), color='red')
graph2.set_title("Indoor Environment\nTemperature and Humidity", color='blue')
graph2.set_xlabel('Temperature', color='green', fontsize=fs)
graph2.set_ylabel('Humidity', color='red', fontsize=fs)
graph2.set_xticks(np.arange(60, 100, step=10))
graph2.set_yticks(np.arange(0, 100, step=10))

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_3c_display_both_temp_humidity.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Review corrleation between derived (rolling mean) data and actual data.</font>
# </div>
# 
# ### <font color = blue size=3>Figure 3d - Display Correlation Heat-Map of Rolling Mean data to Reported data.</font>
# 
# ##### <font color=purple>No real value derived from using Rolling Mean. Just exercise in alter. way to generate heat map.</font>

# In[53]:


merged_df = ext_df.join(int_df, how='left', lsuffix='_out', rsuffix='_in')
data=merged_df.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
#plt.matshow(data)
alpha = ['temp_out', 'hum_out', 'avg_temp', 'avg_hum','temp_in', 'hum_in']
cax = ax.matshow(data, interpolation='nearest')
fig.colorbar(cax)

ax.set_xticklabels([''] + alpha)
ax.set_yticklabels([''] + alpha)

plt.title("Correlation Heat Map\nbetween outdoor weather and indoor environment", color='red')


plt.savefig(my_dir + '/' + 'fig_3d_heatmap_rolldata_2_actual.png')


# <a id='sec3pt4'></a>
# ## <font color=darkblue>Part 4 - Present Composite of weather and environment</font>
# 
# 
# <a href ='#top'>Jump to Table of Contents</a>
# 
# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Present Composite Correlation Plot.</font>
# </div>
# 
# ### <font color = blue size=3>Figure 3e - Display of weather data merged with environment data.</font>

# In[54]:


fs=22
merged_df = ext_df.join(int_df, how='left', lsuffix='_out', rsuffix='_in')
merged_df.plot()
plt.xlabel('Dates', color='green', fontsize=fs)
plt.ylabel("Temperature and Humidity", color='red', fontsize=fs)
plt.title("Composite of findings\nExternal Data and Indoor Data", color='blue', fontsize=fs)

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_3e_composite_outdoor_indoor_temp_n_humidity.png')


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Present Composite Correlation stats.</font>
# </div>
# 
# ### <font color = blue size=3>Table 3d - Display ALL statistics, both derived and real, indoor and outdoor.</font>

# In[55]:


new_df['avg_temp_in'] = new_df['temp'].rolling(10).mean().dropna()
new_df['avg_hum_in'] = new_df['hum'].rolling(10).mean().dropna()
new_df = new_df[abs(stats.zscore(new_df['temp'])) < 2.0]
print(abs(stats.zscore(new_df['hum'])).min())
new_df = new_df[abs(stats.zscore(new_df['hum'])) < 2.0 ]
new_df.replace({'device': {'B8:27:EB:76:5F:45': 'Living Room', 'B8:27:EB:2D:40:28': 'Master Bedroom', 'B8:27:EB:37:B0:F8': 'Guest Bedroom', 'B8:27:EB:A9:D4:C2': 'Kitchen'}}, inplace=True)
new_df.rename(columns={'device': 'room'}, inplace=True)
new_df.set_index(['sysdate'], inplace=True)
merged_df = ext_df.join(new_df, how='left', lsuffix='_out', rsuffix='_in')
merged_df.corr()


# <a id='conclusions'></a>
# <font color=black size=1>=============================================================================================================</font>
# 
# 
# <font color=darkpink size=10>Conclusions</font>
# 
# <font color=black size=1>=============================================================================================================</font>
# 
# <a href ='#top'>Jump to Table of Contents</a>

# <a id='section4'></a>
# # <font color=darkpink>Section 1: Comparative Analysis</font>
# <a href ='#top'>Jump to Table of Contents</a>

# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 1</b> </font><font color=darkblue>: Show the correlation between humidity and temp.</font>
# </div>

# In[56]:


print("#---------------------------------#")
print("External temp correlation to forecast")
print("#---------------------------------#")
print(f"External correlation:",ext_df[['temp', 'forecast']].corr())
print(" ")
print(f"External covariance", ext_df[['temp', 'forecast']].cov())
print(" ")
print("#---------------------------------#")
print("External temp correlation to humidity")
print("#---------------------------------#")
print(f"External correlation:",ext_df[['temp', 'hum']].corr())
print(" ")
print(f"External covariance", ext_df[['temp', 'hum']].cov())
print(" ")
print("#---------------------------------#")
print("Internal temp correlation to humidity")
print("#---------------------------------#")
print(f"Internal correlation", int_df[['temp', 'hum']].corr())
print(" ")
print(f"Internal covariance",  int_df[['temp', 'hum']].cov())
print(" ")
print(" ")
print("#---------------------------------#")
print("Internal temp and humidity correlation to external temp and humidity")
print("#---------------------------------#")
ext_df.corrwith(int_df, axis=0)


# <div class="alert alert-block alert-warning">
#     <b><font color=black>step 2</b> </font><font color=darkblue>: Visualize internal and external variables.</font>
# </div>
# 
#     
# ### <font color = blue size=3>Figure 4a - Overlay of outdoor and indoor correlating data.</font>

# In[57]:


fs=22
ax = mb.plot(kind="scatter", x='hum', y="temp",label="MSTR", c='b', figsize = (22,11))
ax2 = lr.plot(kind="scatter", x='hum', y="temp",label="LIVING", c='orange', ax = ax)
ax3 = gb.plot(kind="scatter", x='hum', y="temp",label="GUEST", c='r' , ax = ax)
ax4 = kt.plot(kind="scatter", x='hum', y="temp",label="KITCHEN", c='brown' , ax = ax)
ax5 = ext_atl.plot(kind="scatter", x='hum', y="temp",label="ATL", c='green' , ax = ax)
ax6 = ext_marietta.plot(kind="scatter", x='hum', y="temp",label="MARI", c='purple' , ax = ax)
ax7 = ext_stonemtn.plot(kind="scatter", x='hum', y="temp",label="STNMTN", c='gray' , ax = ax)
ax8 = ext_coke.plot(kind="scatter", x='hum', y="temp",label="COKE", c='yellow' , ax = ax)
plt.xlabel('humidity', color='green', fontsize=fs)
plt.ylabel('temperature', color='red', fontsize=fs)
plt.title('Composite of all Collected Data\nOutdoor Data overlayed with Indoor Data', color='blue', fontsize=fs)

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_4a_composite_scatter_all.png')


# <a id='sec4pt2'></a>
# # <font color=darkpink>Section 2: Conclusions</font>
# <a href ='#top'>Jump to Table of Contents</a>

# In this project, we used inexpensive parts to collect the indoor's temperature and humidity and queried darksky.net using the Python programming language for weather data. The weather information was only cleaned for missing data, assuming the api provider was sending credible data, whereas the internal data was cleaned using Z-scoring, allowing for 2 standard deviations. 
#    The correlations found were consistent with general weather and environmental properties. Depending on the amount of data pulled, with 5 days being the minimum (yielding over 600 weather records  and over 7,000 environment records per day) , we found a **correlation of -. 91 between the external temperture and humidity. The indoor variables had a -.87 correlation between the external temperature and humidity**. Rolling averages on external temp and humidity were computed and graphed, but were found not to provide any additional insights. With the wide fluctuations on the weather's temp and humidity, we found the environment (internal) temp to remain within a narrow, consistent range of no more than -2 degrees difference between thermostat settings and actual indoor temperature. This suggests that the a/c cooling unit is working at expected capacity, but ventilation and other factors led to non-trivial disparity in cooling each room. **The disparity is supported by the composite correction stats showing only a 37% correlation between the temp indoors and the average temp indoors**(derived from a rolling mean).
#    **These findings suggest making indoor changes to improve cooling efficiencies, and that a stronger a/c unit would not yield any significant value**. Changes include reducing the amount of direct sunlight entering the room, restricting ventilation in rooms which cool below thermostat settings and adding a dehumidifier to supplement the a/c unit's work.

# <a id='sec4pt3'></a>
# # <font color=darkpink>Section 3: Limitations and Future plans</font>
# <a href ='#top'>Jump to Table of Contents</a>

# There are several limitations to this study. First, the **individual sensors were NOT calibrated together so the accuracy of the temperature and humidity are limited to comparing the thermostat setting to the each sensor's thermal report**. During the study, and after 7 days of reporting, the performance of the master bedroom sensor was questioned and then changed from a DHT-11 to a DHT-22 sensor. The **overall impact to reporting was adding high temperature outliers to the data collection pool, while the newly installed sensor self-calibrated**. Calibration time took about 3 minutes. That being said, potential bias from extreme data points collected by the sensors was mimimized by excluding data points exceeding 2 standard deviations. 
#    While data reguarding **other factors known to affect thermal efficiency (i.e. insulation, window panes, etc.) were not collected**, the overall goal of this study was to ascertain whether the a/c was cooling properly and if room specific changes were needed to average out cooling the home, overall. A principle finding of this study was that investment in a new $5,000 a/c system would be premature. With respect to extensions of the current project, the next step is to shrink the data collection elements, so they are plug and play, and replace all dht-11 sensors with AM-312, DS18B20 or DHT-22 sensors. The largest challenge lies in setting up the wifi on each collection device, although not arduous for setting up within a home, anything larger could prove to be task intensive. . 
#    
# Another domestic, indoor test will commence with the onset of winter in order to study and maximize heating efficiencies. We are researching how to economically build an interface that actually tracks when the HVAC engages, as well as a watchdog program running on the Raspberry Pi, that will e-mail the homeowner when indoor temperature is below or above the thresholds set by the homeowner.
# 
# Other plans are to set up agricultural solution, measuring both outside temp and inside a hothouse or nursery. 

# ### <font color = blue size=3>Figure 5a - Limitation of master bedroom sensor gone awry.</font>

# In[58]:


fs=22
plt.rcParams['figure.figsize'] = (16,12)
plt.rcParams['font.size'] = 15

x = mb['hum']

y = mb['temp']

plt.plot(x, y, color='orange', label='time series path')
plt.scatter(x, y, label='Master Bedroom (mb)', color='b', s=250, marker='x')



plt.xlabel('Humidity', color='green', fontsize=fs)
plt.ylabel('Temperature', color='red', fontsize=fs)
plt.title('Master bedroom temperature and humidity graph\nshowing erratic findings before replacing sensor\nand high temperature outliers from replacement sensor self-calibration', color='blue', fontsize=fs)
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2)
plt.legend()

if my_dir:
    plt.savefig(my_dir + '/' + 'fig_5a_limitation_mstrbed_sensor_awry.png')

