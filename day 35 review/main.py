import requests

parameters = {
   "lat" : 51.507351,
    "lon" : -0.127758,
    "appid" : "52327fc84eb696f3ed6ab6f0df327001",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)

# print(response.status_code)

data = response.json()
# print(data)

weather = data["hourly"][8]["weather"][0]["main"]
print(weather)
