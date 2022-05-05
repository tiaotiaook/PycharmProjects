import requests

reponses = requests.get(url="http://api.open-notify.org/iss-now.json")

print(reponses.status_code)
# 打印的是回应代码

data = reponses.json()
print(data)

# 用json的格式获取数据

longitude = reponses.json()["iss_position"]["longitude"]
latitude = reponses.json()["iss_position"]["latitude"]

# 创建元组
iss_position = (longitude,latitude)
print(iss_position)
