import random
from time import sleep
from Score import add_score


def _screen_cleaner():
    print("\n" * 20)


def difficulty_Memory():
    difficulty = int(input("Now please select difficulty 1 to 3: "))
    if difficulty == 1:
        print(f"You selected: Memory Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Memory_Game1()
    elif difficulty == 2:
        print(f"You selected: Memory Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Memory_Game2()
    elif difficulty == 3:
        print(f"You selected: Memory Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Memory_Game3()
    elif difficulty > 3 or difficulty <= 0:
        print("You must to select only from 1 to 3!")
        return difficulty_Memory()


def Memory_Game():
    print("You selected Memory Game!")
    difficulty_Memory()


def Print_Memory_Wellcom():
    print("We are gonna role a cube with numbers")
    print("You will have a couple of seconds to remember the number")
    print("Starting now...")


def Start_Memory_Game1():
    Print_Memory_Wellcom()
    sleep(2)
    x = random.randint(0, 9)
    print(x)
    sleep(3)
    _screen_cleaner()
    y = int(input("What was the number? "))
    if x == y:
        print("You Got it right! Well Done!")
        add_score(1)
    elif x != y:
        print("Bop, That wrong. Try next time!")


def Start_Memory_Game2():
    Print_Memory_Wellcom()
    sleep(2)
    x = random.randint(0, 9)
    print(x)
    sleep(1.5)
    _screen_cleaner()
    y = int(input("What was the number? "))
    if x == y:
        print("You Got it right! Well Done!")
        add_score(2)
    elif x != y:
        print("Bop, That wrong. Try next time!")


def Start_Memory_Game3():
    Print_Memory_Wellcom()
    sleep(2)
    x = random.randint(0, 9)
    print(x)
    sleep(0.7)
    _screen_cleaner()
    y = int(input("What was the number? "))
    if x == y:
        print("You Got it right! Well Done!")
        add_score(3)
    elif x != y:
        print("Bop, That wrong. Try next time!")
