import requests

# 生成的api是https://opentdb.com/api.php?amount=10&type=boolean，但是只需要问号前面的部分
# 剩下的部分是params的参数  ?amount=10&type=boolean

parameters = {
   "amount":10,
    "type":"boolean",
}


response = requests.get(url="https://opentdb.com/api.php",params=parameters)

response.raise_for_status()
data = response.json()
question_data = data["results"]

# print(data)