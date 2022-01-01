# print("welcome to the rollercoaster !")
# height = int(input("what is your  height in cm ?"))
#
# bill = 0
#
# if height > 120:
#     print("you can ride.")
#
#     age = int(input("what is your age ?"))
#
#     if age <= 12:
#         bill = 5
#     elif 12 < age <=18:
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("have free")
#
#     else:
#         bill = 12
#
#     answer = input("want photos ? Y or N")
#
#     if answer =="Y":
#         bill += 3
#
#     print(f"your bill is {bill}$.")
#
#
# else:
#     print("you can't ride.")


print("welcome to tresure island.\nyour mission is to find the treasure.")
choice1 = input('you are at a crossroad,where do you want to go ? type "left" or "right"').lower()
if choice1 == "left":
    choice2 = input('you come to a lake,  "swim" or "wait" ').lower()
    if choice2 == "wait":
        choice3 = input("what color ? red yellow or blue?").lower()
        if choice3 == "yellow":
            print("you win")
        elif choice3 == "red":
            print("burned by fire,game over.")
        elif choice3 == "blue":
            print("eaten by beasts ,game over.")
        else :
            print("the door not exist,game over.")


    else:
        print("attacked by an angry trout,game over")

else:
    print("fell into a hole. game over." )

