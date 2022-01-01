import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("welcome to the pypassword generator!")
long = int(input("how many letters would you like in your password?"))
sym = int(input("how many symbols would you like ?"))
num = int(input("how many numbers would you like ?"))

password_list = []

for n in range(sym):
    password_list.append(random.choice(symbols))

for n in range(num):
    password_list.append(random.choice(numbers))

for n in range((long - sym - num)):
    password_list.append(random.choice(letters))


print(password_list)

random.shuffle(password_list)



password = ""

for n in password_list:
    password += n


print(f"here is your password:{password}")





# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# # print(student_heights)
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)
# # 🚨 Don't change the code above 👆
#
#
# #Write your code below this row 👇
# long = 0
# students = 0
# for n in student_heights:
#     long += n
#
# for n in student_heights:
#     students += 1
#
# avg = round(long/students)
# print(avg)



# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# high = 0
#
# for n in student_scores:
#     if n > high :
#         high = n
#
# print(high)

# sum = 0
# for n in range(1,101):
#     sum += n
# print(sum)

# for n in range(1,11,3):
#     print(n)

# sum = 0
# for n in range(1, 101):
#     if n % 2 ==0 :
#         sum += n
# print(sum)




# for n in range(1, 101):
#     if n % 3 == 0 and n % 15 != 0:
#         print("fizz")
#
#     elif n % 5 == 0 and n % 15 != 0:
#         print("buzz")
#
#     elif n % 15 == 0:
#         print("fizzbuzz")
#
#     else:
#         print(n)
