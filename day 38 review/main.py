import requests
from datetime import datetime


Application_ID="4b17e3a1"
Application_Keys="974eb668cec90a053edc4f335fbec48a"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/6724479fa3264e21b26440c6b780880e/myWorkoutsCopy/workouts"


exercise_text = input("Tell me which exercises you did: ")

headers ={
    "x-app-id":Application_ID,
    "x-app-key":Application_Keys,

}

post_para={
    "query":exercise_text,
    "gender":"female",
    "weight_kg":50,
     "height_cm":160,
    "age":27
}

response = requests.post(exercise_endpoint,json=post_para,headers=headers)

result = response.json()

# print(result)

# 格式转换
# https://www.w3schools.com/python/python_datetime.asp
today_date = datetime.now().strftime("%d/%m/%Y")
# e.g. 17:41:00
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Basic dGlhb3RpYW86MDQxMjAzOTQxODU0"
}

# 记录时间 以及换算
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    #
    # print(sheet_response.text)



    sheet_response = requests.post(sheet_endpoint,json=sheet_inputs,headers=bearer_headers)
    print(sheet_response.text)

