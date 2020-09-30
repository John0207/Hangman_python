'''
This is a hangman gme from the book
The self-taught programmer by Cory Althoff
'''


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
