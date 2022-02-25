import requests
from twilio.rest import Client

own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "52327fc84eb696f3ed6ab6f0df327001"

account_sid = "AC23d49f9dfa119090b94a9d5bad9e60ae"
auth_token = "d7e9ec423247361c4718acbf29ef894c"


weather_params ={
    "lat":31.2222,
    "lon":121.4581,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(own_endpoint,params=weather_params)

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]


will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 900:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="it is going to rain, remember to bring an umbrella☔ ",
        from_='+18592956541',
        to='+8618810227406'
    )

    print(message.status)









