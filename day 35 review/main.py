
import requests
import os
from twilio.rest import Client

account_sid = 'AC23d49f9dfa119090b94a9d5bad9e60ae'
auth_token ='491404b7fab17b69056c5b5addc113b3'

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
#
# auth_token = os.environ['TWILIO_AUTH_TOKEN']



# part 1 获取


parameters = {
   "lat" : 51.507351,
    "lon" : -0.127758,
    "appid" : "52327fc84eb696f3ed6ab6f0df327001",
    # 只需要hourly，所以除了以下三项
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)

# print(response.status_code)

weather_data = response.json()
# print(weather_data)



# part 2 天气代码小于700，需要带伞

# hour_weather = weather_data["hourly"][0]["weather"][0]["id"]
# 只需要未来12小时数据
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

#只需要未来12小时数据的天气代码

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain=True


# part 3 发送短信

if will_rain:
    print("take umbrella")
    client = Client ( account_sid, auth_token )
    message = client.messages \
        .create (
        body="take umbrella",
        from_='+18592956541',
        to='+8618810227406'
    )

    print(message.status)


