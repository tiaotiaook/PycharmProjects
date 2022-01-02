import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

# num = random.choice(cards)
# print(num)


for n in range(2):
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

print(user_cards)
print(computer_cards[0])
# score = sum(user_cards)
# print(score)
print(f"your cards :{user_cards}, current score {sum(user_cards)}.")
print(f"computer first card is: {computer_cards[0]}")


if sum(user_cards) == 21:
    print("you win")
elif sum(computer_cards) == 21:
    print("computer win")



else:
    go_on = input("type 'y' to get another card, or 'n' to pass :")

    if go_on == "y":
        user_cards.append(random.choice(cards))
        print(f"your cards :{user_cards}, current score {sum(user_cards)}.")
        if sum(user_cards) == 21:
            print("you win")
        elif sum(user_cards) > 21:
            print("you lose")




    elif go_on == "n":
        print(f"your final hand:{user_cards}, final score :{sum(user_cards)}")
