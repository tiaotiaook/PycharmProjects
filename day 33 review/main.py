import requests
#
# # reponses = requests.get(url="http://api.open-notify.org/iss-now.json")
# #
# # print(reponses.status_code)
# # # 打印的是回应代码
# #
# # data = reponses.json()
# # print(data)
# #
# # # 用json的格式获取数据
# #
# # longitude = reponses.json()["iss_position"]["longitude"]
# # latitude = reponses.json()["iss_position"]["latitude"]
# #
# # # 创建元组
# # iss_position = (longitude,latitude)
# # print(iss_position)
#
MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
}

response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()

data = response.json()
print(data)

# import requests
# from datetime import datetime
#
# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)