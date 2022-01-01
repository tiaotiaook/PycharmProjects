#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result  = {word:len(word) for word in sentence.split()}
#
#
# print(result)



# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {day:(temp *9/5) + 32 for (day,temp) in weather_c.items()}
#
# print(weather_f)


student_dict = {
    "student":["angela","james","lily"],
    "score":[56,76,98]
}
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for(index,row) in student_data_frame.iterrows():
    # print(row.score)
    if row.student == "angela":
        print(row.score)