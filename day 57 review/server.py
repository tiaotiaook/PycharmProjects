from flask import Flask, render_template
import random
import datetime
import requests

# year = datetime.datetime.now()
# year_1 =year.strftime("%Y")




app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html",num=random_number,t=current_year)


@app.route('/guess/<name>')
def guess(name):
    gender_url=f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender=gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]


    return render_template("guess.html",name=name,gender=gender,age=age)


if __name__ == "__main__":
    app.run(port =7001 ,debug=True)

#
# from flask import Flask, render_template
# import requests
#
# app = Flask(__name__)
#
# response_1 = requests.get(url="https://api.agify.io")
# response_2 = requests.get(url="https://api.genderize.io")
#
# age=response_1.json()["age"]
#
# gender=response_1.json()["gender"]
#
# # age_api = "https://api.agify.io"
# # x_api = "https://api.genderize.io"
#
# @app.route('/guess/<name>')
# def guess(name):
#
#     return render_template("index.html",xingbie= gender, num=age)
#
#
# if __name__ == "__main__":
#     app.run(port =7001 ,debug=True)