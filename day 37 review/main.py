
import requests
from datetime import datetime

# requests.get()  requests.post()  requests.put()   requests.delete()
USERNAME="tiaotiaotiao"
TOKEN="sjdbjkgrk"
GRAPH_ID ="tiaotiaodawang"

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

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)



# 打卡

post_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# 倒入时间模块，但是需要整理post需要的格式  strftime

today= datetime.now()


post_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"22.5",
}


# response = requests.post(url=post_endpoint,json=post_config,headers=headers)



# update pixela

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


update_config = {
    "quantity": "0.5",
}


# response = requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)


# delete pixela

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# update_config = {
#     "quantity": "0.5",
# }


response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)