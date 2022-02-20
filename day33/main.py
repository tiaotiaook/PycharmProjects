import requests
from datetime import datetime
import smtplib

my_email = "shihuaok@gmail.com"
my_password = "041203941854ysh"


my_lat = 31.230391
my_lng = 121.473701

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])


    if my_lat-5 <= iss_latitude <= my_lat+5 and my_lng -5 <= iss_longitude <= my_lng + 5:
        return True

def is_night():

    parameters = {
        "lat":my_lat,
        "lng":my_lng,
        "formatted" : 0
    }

    reponse = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    reponse.raise_for_status()
    data = reponse.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    print(time_now.hour)

    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email,my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="2830554908@qq.com",
        msg = "Subject:look up\n\n th iss is above you in the sky."
    )



