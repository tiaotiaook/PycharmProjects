from game_data import data
import random
from replit import clear

num_1 = random.choice(data)
print(num_1)
print(f"compare a : {num_1['name']} , a {num_1['description']} , from {num_1['country']}")
num_1_follower = num_1['follower_count']
print(num_1_follower)


num_2 = random.choice(data)
print(num_2)
print(f"compare b : {num_2['name']} , a {num_2['description']} , from {num_2['country']}")
num_2_follower = num_2['follower_count']
print(num_2_follower)

answer = input("who has more followers? a or b :").lower()

