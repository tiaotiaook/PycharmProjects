import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

def is_iss_overhead():

    reponses = requests.get(url="http://api.open-notify.org/iss-now.json")

    # print(reponses.status_code)
    # # 打印的是回应代码

    data = reponses.json()
    # print(data)

    # 用json的格式获取数据

    longitude = float(data["iss_position"]["longitude"])
    latitude = float( data["iss_position"]["latitude"])

    # 创建元组
    # iss_position = (longitude,latitude)
    # print(iss_position)

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG - 5 <= longitude < MY_LONG + 5:
        return True


def is_night():

    parameters = {
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()
    # print(data)
    # 日出日落时间
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    # 现在的时间，但是格式不一样，是24h，需要转换
    time_now = datetime.now().hour
    print(time_now)

    # 判断是否天黑
    if time_now>= sunset or time_now<= sunrise:
        return True


# 当日落后，经纬度偏差在5度之内，OK

if is_iss_overhead() and is_night():
    print("lookup")
else:
    print("don't look up")
