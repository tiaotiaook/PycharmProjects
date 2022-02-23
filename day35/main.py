import requests

own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "52327fc84eb696f3ed6ab6f0df327001"


weather_params ={
    "lat":31.2222,
    "lon":121.4581,
    "appid":api_key

}

response = requests.get(own_endpoint,params=weather_params)

data = response.json()

print(data)






