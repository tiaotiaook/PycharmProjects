letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode():
    new_list = []
    list1 = list(message)
    for n in range(len(message)):
        new_list.append(letter_list[letter_list.index(list1[n]) + number])

    new_words = "".join(new_list)
    print(new_words)

def decode():
    new_list = []
    list1 = list(message)
    for n in range(len(message)):
        new_list.append(letter_list[letter_list.index(list1[n]) - number])

    new_words = "".join(new_list)
    print(new_words)

end_of_game = False
while not end_of_game:
    choice = input("type 'encode' to encrypt,type 'decode' to decrypt:")
    message = input("type your message :")
    number = int(input("type the shift number :"))
    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()

    go_on = input("type 'yes' if you want to go again,or type 'no'.")
    if go_on == "yes":
        end_of_game = False
    elif go_on == "no":
        end_of_game = True








