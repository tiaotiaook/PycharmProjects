import requests

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


pixel_data = {
    "date":"20220227",
    "quantity":"15.8"

}

response = requests.post(url = pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)