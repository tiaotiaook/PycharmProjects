from game_data import data
import random



num_1 = random.choice(data)
print(num_1)
print(f"compare A: {num_1['name']} , a {num_1['description']}, from {num_1['country']}.")
print("VS")
num_2 = random.choice(data)
print(num_2)
print(f"compare B: {num_2['name']} , a {num_2['description']}, from {num_2['country']}.")



def compare(answer,a,b):
        if answer == "A":
            if num_1['follower_count'] > num_2['follower_count']:
                score += 1
                print(f"you are right ,current score is {score}")
                return False
            else:
                print(f"that is wrong. your final score: {score}")
                return True
        elif answer == "B":
            if num_1['follower_count'] > num_2['follower_count']:
                print(f"that is wrong. your final score: {score}")
                return True
            else:
                score += 1
                print(f"you are right ,current score is {score}")
                return False


compare(num_1,num_2)
end_of_game = False
while not compare(num_1,num_2):
    num_3 = random.choice(data)



