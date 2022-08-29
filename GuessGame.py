import random
from time import sleep
from Score import add_score


def difficulty_Guess():
    difficulty = int(input("Now please select difficulty 1 to 3: "))
    if difficulty == 1:
        print(f"You selected: Guess Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Guess_Game1()
    elif difficulty == 2:
        print(f"You selected: Guess Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Guess_Game2()
    elif difficulty == 3:
        print(f"You selected: Guess Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Guess_Game3()
    elif difficulty > 3 or difficulty <= 0:
        print("You must to select only from 1 to 3!")
        return difficulty_Guess()


def Guess_Game():
    print("You selected Guess Game!")
    difficulty_Guess()


def Print_Guess_Welcome():
    print("welcome to the Guess Game!")
    print("I will think about number and you will need to Guess in")
    print("It can't be a minus! Starting now...")


def Start_Guess_Game1():
    Print_Guess_Welcome()
    sleep(2)
    print("I'm thinking about a number from 1-3")
    sleep(2)
    x = random.randint(1, 3)
    y = int(input("What is the number? "))
    if x == y:
        print("You Got it right! Well Done!")
        add_score(1)
    elif x != y:
        print("Bop, That wrong. Try next time!")


def Start_Guess_Game2():
    Print_Guess_Welcome()
    sleep(2)
    print("I'm thiking about a number from 1-5")
    sleep(2)
    x = random.randint(1, 5)
    y = int(input("What is the number? "))
    if x == y:
        print("You Got it right! Well Done!")
        add_score(2)
    elif x != y:
        print("Bop, That wrong. Try next time!")


def Start_Guess_Game3():
    Print_Guess_Welcome()
    sleep(2)
    print("I'm thiking about a number from 1-7")
    sleep(2)
    x = random.randint(1, 7)
    y = int(input("What is the number? "))
    if x == y:
        print("You Got it right! Well Done!")
        add_score(3)
    elif x != y:
        print("Bop, That wrong. Try next time!")
