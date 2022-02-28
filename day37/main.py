import requests
from datetime import datetime

TOKEN = "jkgkjfjhfghdugk"
USER_NAME = "shihua"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url = pixela_endpoint,json = user_params)
# print(response.text)

graph_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {

    "id":"GRAPH_ID",
    "name":"meditation",
    "unit":"mins",
    "type":"float",
    "color":"shibafu"
}

headers = {"X-USER-TOKEN":TOKEN}

# response = requests.post(url=graph_endpoint,json = graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many kilometers did you cycle today?")
}

response = requests.post(url = pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


new_pixel_data = {
    "quantity": "3.5"
}

# response = requests.put(url = update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url = delete_endpoint,headers= headers)
# print(response.text)