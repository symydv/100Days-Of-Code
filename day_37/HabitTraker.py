import requests
from datetime import datetime

TOKEN = "ajdskfajfiaemo"
USERNAME = "sym124"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN, #create your own username and token
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_confi = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_confi, headers = headers)

# #.post() is used to post something on website..

# print(response.text)


today = datetime.now()
print(today.strftime("%Y%m%d")) #it will give use date in formate yyyymmdd , in string formate.

data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config ={
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "30",
}

# response = requests.post(url=data_endpoint, json=pixel_config, headers = headers)

# print(response.text)




#Using .put() we can update our data like in this case we can update our pixel on any date..

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "4.5"
}


response = requests.post(url=update_endpoint, json=new_pixel_data, headers = headers)

print(response.text)




#.delete() is used to delete any pixel

"""you can use documentation of api to use any of these 4 methods."""
