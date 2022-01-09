from game_data import data
import random
from replit import clear

def check_k(answer, a, b):
    if answer == "a":
        if a > b:
            return True
        else:
            return False
    elif answer == "b":
        if a > b:
            return False
        else:
            return True

score = 0
game_continue = True
num_2 = random.choice(data)


while game_continue:
    num_1 = num_2
    num_1_follower = num_1['follower_count']
    print(num_1_follower)
    print(f"compare A: {num_1['name']} , a {num_1['description']}, from {num_1['country']}.")

    print("VS")

    num_2 = random.choice(data)
    num_2_follower = num_2['follower_count']
    print ( num_2_follower )
    print ( f"compare B: {num_2['name']} , a {num_2['description']}, from {num_2['country']}." )


    answer = input("who has more followers? type 'a' or 'b' : ").lower()

    is_correct = check_k(answer,num_1_follower,num_2_follower)

    clear()

    if is_correct:
        score += 1
        print(f"you are right. your score is {score}")

    else:
        game_continue = False
        print(f"you are wrong.your score is {score}")


