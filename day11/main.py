import random
from replit import clear

# 创建发牌函数
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# 创建计算总和函数，如果和=21且只有两张牌，返回0，如果和大于21，11变成1

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# 创建比较函数 相等、其中一个=0，也就是21了、爆掉、大于、小于

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "you lose , opponent has blackjack"
    elif user_score == 0:
        return "you win"
    elif computer_score > 21:
        return "you win,opponent went over"
    elif user_score > 21:
        return "you went over ,you lose"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


# 创建游戏函数，创建空列表、游戏没结束，发两张牌，用户是否发牌，电脑是否发牌17，打印并且比较

def play_game():

  user_cards = []
  computer_cards = []
  is_game_over = False

  for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  # print(user_cards)
  # print(computer_cards)

  while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:

            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

  while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      clear()
      play_game()

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_cards = []
# computer_cards = []
#
# # num = random.choice(cards)
# # print(num)
#
#
# for n in range(2):
#     user_cards.append(random.choice(cards))
#     computer_cards.append(random.choice(cards))
#
# print(user_cards)
# print(computer_cards[0])
# # score = sum(user_cards)
# # print(score)
# print(f"your cards :{user_cards}, current score {sum(user_cards)}.")
# print(f"computer first card is: {computer_cards[0]}")
#
#
# if sum(user_cards) == 21:
#     print("you win")
# elif sum(computer_cards) == 21:
#     print("computer win")
#
#
#
# else:
#     go_on = input("type 'y' to get another card, or 'n' to pass :")
#
#     if go_on == "y":
#         user_cards.append(random.choice(cards))
#         print(f"your cards :{user_cards}, current score {sum(user_cards)}.")
#         if sum(user_cards) == 21:
#             print("you win")
#         elif sum(user_cards) > 21:
#             print("you lose")
#
#
#
#
#     elif go_on == "n":
#         print(f"your final hand:{user_cards}, final score :{sum(user_cards)}")
