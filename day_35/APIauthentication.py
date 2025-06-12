#API can be free or  paid.
#API key are used by api providers to track your use of api..

import requests
from twilio.rest  import Client
#For  Twilio ########################################################
Account_SID = "ACc88bcf1f901edb2e17095bb04dae5813"
Auth_token = "a25bee98f0d9ac46c3c451d30fae5f38"
Twilio_phone_number = "+16507191050"
#################################################################


MY_LAT = 16.833628 # Your latitude
MY_LONG = 81.530850 # Your longitude

api_key = "2d5869cc56dcd4d260a4480a4c153811" #this api key to use  current weather data.


req = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=16.833628&lon=81.530850&appid=2d5869cc56dcd4d260a4480a4c153811")

'''We have to get hourly data for next 12 hours to get information about rain 
    but for that we require one call api which is not working for unknown reasons'''


json_file = req.json()
weather = json_file["weather"]

if weather[0]["id"]<=700: #this means rain.
    client = Client(Account_SID, Auth_token)
    message = client.messages \
        .create(
            body="Bring an umbrella it might rain",
            from_="+16507191050",
            to="your number"
        )
    print(message.status)
else:
    client = Client(Account_SID, Auth_token)
    message = client.messages \
        .create(
            body="No rain today",
            from_="+16507191050",
            to="your number"
        )
    print(message.status)



print(json_file)






 