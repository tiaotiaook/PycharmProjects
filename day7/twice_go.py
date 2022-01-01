import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# chosen_word = word_list[0]
print(chosen_word)

display = []

for n in range(len(chosen_word)):
    display.append("_")
print(display)

lives = 6

# ======================================

end_of_game = False
while not end_of_game:
    guess = input("guess a letter ? :").lower()

    if lives > 1:

        if guess in chosen_word:

            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = guess
            print(display)
            print(lives)

        elif guess not in chosen_word:
            print(display)
            lives -= 1
            print(lives)

        if "_" not in display:
            end_of_game = True
            print("you win")

    else:
        end_of_game = True
        print("lose")










