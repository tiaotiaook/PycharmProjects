# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # print(data)
#     for row in data:
#
#         # 打印每一行
#         # print(row)
#
#         # 打印每一行的第二个元素，也就是温度，但是会出现第一行的标签，也就是temp
#         # print(row[1])
#
#         #这种可以，但是打印出来的是一列
#         # if row[1] != "temp":
#         #     print(row[1])
#
#         #现在要打印出来的是一行
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# 计算平均数，但是很麻烦
# a = sum(temp_list)
# average =a /(len(temp_list))
# print(average)

# 调用panda函数mean()计算平均数、最大值
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# 调取【行】
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)

# 创建数据框架
# data_dict = {
#     "student" : ["Amy","James","Angela"] ,
#     "score" : [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv ("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")
