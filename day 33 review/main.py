import requests
from datetime import datetime
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
    "formatted":0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()
print(data)
# 日出日落时间
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

# 现在的时间，但是格式不一样，是24h，需要转换
time_now = datetime.now()
print(time_now.hour)