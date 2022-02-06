numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number*number for number in numbers]

#Write your code 👆 above:

print(squared_numbers)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

# result = [num for num in numbers if num%2==0]

#Write your code 👆 above:

# print(result)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# new_dict = {new_key:new_value for (key,value) in dict.item if test}
# Write your code below:

# convert a sentence into a list of words
dictory = sentence.split()
print(dictory)

new_dict = {word: len(word) for word in dictory}

print(new_dict)
#
# names = ["jsgd","suigdu","shd","shgdkbcjkw","sjgc","hs","hfhhj"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passed_student = {student: score for (student,score) in students_scores.items() if score > 60}
# print(passed_student)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {xingqi : float((temp*9/5)+32) for (xingqi,temp) in weather_c.items()}

print(weather_f)