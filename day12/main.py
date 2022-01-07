# enemies = 1
# def increase_enemies():
#
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
# enemies = increase_enemies()
#
# print(f"enemies outside function: {enemies}")


# The number guessing game

import random

number = random.randint(1,100)
print(number)
lives = 5

def guess_number_game(lives):

    end_of_game = False
    while not end_of_game:
        num_1 = int(input("make a guess："))
        if lives > 1:
            if num_1 == number:
                print("you win")
                end_of_game = True
            elif num_1 < number:
                print("too low")
                lives -= 1
                print("guess again")
                print(f"you have {lives} attempts remaining.")
            elif num_1 > number:
                print("too high")
                lives -= 1
                print ( "guess again" )
                print ( f"you have {lives} attempts remaining." )
        else:
            print("run out of guesses, you lose")
            end_of_game = True

mode = input("choose a difficulty ,easy or hard?")
if mode == "hard":
    lives = 5
elif mode == "easy":
    lives == 10

print(f"you have {lives} attempts remaining.")
guess_number_game(lives)

