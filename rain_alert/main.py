import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "52327fc84eb696f3ed6ab6f0df327001"

weather_params = {
    "lat":"51.759050",
    "lon":"19.458600",
    "appid": api_key,
    "exclude":"current,minutely,daily"

}

response = requests.get(OWN_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    print("bring an umbrella.")

# print(weather_slice)
# print(weather_data["hourly"][0]["weather"][0]["id"])