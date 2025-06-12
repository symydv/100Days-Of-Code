#API - Application Programing Interface
'''It is a set of commands, functions, protocols and objects
    that programmers can use to create software or 
    interact with an external system.'''

import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# #print(response.status_code) # .status_code gives use status code like if its wrong api it will give 404 and if its correct it will give 200.
# #you can check more about status code on http status code.

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude,latitude)

# print(iss_position)

##################################################################################################
#sunrise and sunset 
#(This server requires Latitude(lat) and Longitude(lng) as parameter)

parameters ={
    "lat" : 16.833628,
    "lng" : 81.530850
}


response=  requests.get("https://api.sunrisesunset.io/json", params= parameters)

data = response.json()
sunrise = data["results"]["sunrise"]
print(data)