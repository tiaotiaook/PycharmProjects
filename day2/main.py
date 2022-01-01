print("welcome to the tip calculator")
total_bill = float(input("what is the total bill ?$"))
people = int(input("how many people to split the bill ?"))
percentage = int(input("what percentage tip would you like to give ? 10,12or 15?"))
pay = round((total_bill*(1+percentage/100))/people,2)
final_pay = "{:.2f}".format(pay)
print(f"each people should pay:${final_pay}")




# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# name = name1 + name2
# name_lower = name.lower()
#
# t_times = name_lower.count('t')
# r_times = name_lower.count('r')
# u_times = name_lower.count('u')
# e_times = name_lower.count('e')
#
# l_times = name_lower.count('l')
# o_times = name_lower.count('o')
# v_times = name_lower.count('v')
#
# number_1 = t_times + r_times + u_times + e_times
# number_2 = l_times + o_times + v_times + e_times
#
# score = number_1*10 + number_2
#
# if score<10 or score>90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40<score<50:
#     print(f"Your score is  {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

# name = input("what is your name ? ")
# name_lower = name.lower()
# print(name_lower)

#
# age=12
# print("your are" + str(age) +"years old")

# name = input("what is your name?")
# print("hello,"+name)