import smtplib
import datetime as dt
import random

MY_EMAIL = "shihuaok@gmail.com"
MY_PASSWORD = "041203941854"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 4:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"subject:Monday Motivation\n\n{quote}"
        )








year = now.year

# if year == 2021:
#     print("wear a face mask")

week_day = now.weekday()

print(day_of_week)

date_of_birth = dt.datetime(year=1995,month=12,day=15,hour=4)
print(date_of_birth)