# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)



# data = pandas.read_csv("weather_data.csv")

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp* 9/5 +32
# print(monday_temp_f)



# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)


# t = 0
# for temp in temp_list:
#     t += temp
# s = t/len(temp_list)
# print(s)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)




# data_dict = {
#     "student":["amy","james","angela"],
#     "scores":[76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gery_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gery_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "color":["Gray","Cinnamon","Black"],
    "count":[gery_squirrels_count,red_squirrels_count,black_squirrels_count]

}
print(data_dict)

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

