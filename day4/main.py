import random
import my_moudle

# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_moudle.pi)

# random_float = random.random()
# print(random_float)

# random_side = random.randint(0,1)
# if random_side == 1:
#     print("Heads")
# else :
#     print("Tails")


name_string = input("give me everybody's names, seperated by a comma")

names = name_string

name_list = names.split(",")

# who = name_list[random.randint(0,len(name_list))-1]
who = random.choice(name_list)

print(f"{who} will pay for the meal.")


# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
#
# map =[row1,row2,row3]
#
# # print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure?")
#
# # colunmn 列 row 行
#
# colunmn = int(position[0])
# row = int(position[1])
#
# map[colunmn-1][row-1] = "*"
#
#
# print(f"{row1}\n{row2}\n{row3}")




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play_list = [rock, paper, scissors]

user_choice = int(input("what do you choose? 0 for rock,1 for paper or 2 for scissors. "))
print(play_list[user_choice])

computer_choice = random.randint(0,2)
print("computer choice:")
print(play_list[computer_choice])


if user_choice == computer_choice:
    print("draw")
elif (computer_choice == 0 and user_choice == 1) or (computer_choice == 2 and user_choice == 1) or (computer_choice == 1 and user_choice == 2):
    print("you win.")
elif user_choice>=3 or user_choice < 0:
    print ( "You typed an invalid number, you lose!" )
else :
    print("you lose.")




