'''
This is a hangman game from the book
The self-taught programmer by Cory Althoff
'''
from random import randint


def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|        |          ",
              "|        0          ",
              "|       /|\         ",
              "|       / \         ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome To Hangman")
    print(word)

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess one letter at a time: "
        char = input(msg).lower().strip()
        char = char[0]
        if char in rletters:
            print(char)
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            print(char)
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was " + word)


word_list = ["apples", "bananas", "strawberries", "kiwis", "pears", "pineapples"]
word = word_list[randint(0, (word_list.__len__())) - 1]
hangman(word)
