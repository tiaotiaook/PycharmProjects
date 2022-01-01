import random
from replit import clear
word_list = ["aardvark", "baboon", "camel"]

lives = 6

# chosen_word = random.choice(word_list)
chosen_word = word_list[0]
print(chosen_word)

display = []
for n in range(len(chosen_word)):
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("guess a letter?:").lower()

    clear()

    if guess in display:
            print(f"you have already guessed:{guess}")

    for position in range(len(chosen_word)):
            letter = chosen_word[position]
            # print(f"current position: {position}\n current letter :{letter}\n guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

    if guess not in chosen_word:
            print(f"you guessed:{guess},not in the word,you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("you lose")

    print(f"{''.join(display)}")

    if "_" not in display:
            end_of_game = True
            print("you win")









 # for letter in chosen_word:
        #
        #     if letter == guess:
        #         display[chosen_word.index(letter)] = guess
        # # 这个方法不行，因为chosen_word.index(letter)永远返回的是第一个 a 的位置，不会更新
        # print(display)