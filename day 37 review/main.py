
import requests

# requests.get()  requests.post()  requests.put()   requests.delete()
USERNAME="tiaotiaotiao"
TOKEN="sjdbjkgrk"

pixela_endpoint = "https://pixe.la/v1/users"

# 创建账户
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}
# requests.post()和requests.get()，是相反的两个过程
# response = requests.post(url=pixela_endpoint,json=user_params)
#
# print(response.text)

# 创建一个graph
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"tiaotiaodawang",
    "name":"tiaotiao's commit",
    "unit":"commit",
    "type":"float",
    "color":"sora",
}

headers ={
    "X-USER-TOKEN":TOKEN
}

response = requests.post(url=graph_endpoint,json=graph_config)