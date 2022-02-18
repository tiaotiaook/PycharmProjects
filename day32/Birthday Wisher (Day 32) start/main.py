# import smtplib
#
# my_email = "shihuaok@gmail.com"
# password = "041203941854ysh"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="2830554908@qq.com",
#                         msg="Subject:Hello\n\nhappy birthday to you!")

# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# if year == 2022:
#     print("wear a face mask")


import smtplib
import datetime as dt
import random


my_email = "shihuaok@gmail.com"
password = "041203941854ysh"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="2830554908@qq.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )








