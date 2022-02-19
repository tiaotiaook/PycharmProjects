##################### Normal Starting Project ######################

from datetime import datetime
import pandas
import random
import smtplib

email = "shihuaok@gmail.com"
password = "041203941854ysh"
# 2. Check if today matches a birthday in the birthdays.csv

today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:happy!\n\n{contents}")





