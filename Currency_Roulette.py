import random
from time import sleep
# pip install forex-python (is must for installing)
from forex_python.converter import CurrencyRates

c = CurrencyRates()


def difficulty_Currency():
    difficulty = int(input("Now please select difficulty 1 to 3: "))
    if difficulty == 1:
        print(f"You selected: Guess Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Currency_Game1()
    elif difficulty == 2:
        print(f"You selected: Guess Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Currency_Game2()
    elif difficulty == 3:
        print(f"You selected: Guess Game! and {difficulty} difficulty level")
        print("Lets start...")
        Start_Currency_Game3()
    elif difficulty > 3 or difficulty <= 0:
        print("You must to select only from 1 to 3!")
        return difficulty_Currency()


def Currency_Roulette():
    print("You selected Currency Roulette!")
    difficulty_Currency()


def Print_Currency_Welcome():
    print("Welcome to the Currency Roulette!")
    print("Here you will need to guess the Currency rate")
    print("Starting now...")


def Start_Currency_Game1():
    Print_Currency_Welcome()
    sleep(1.5)
    print("Difficulty 1 - you can get wrong between +1 or -1")
    print("Example: Your answer is 1.5 but the rate is 0.8 so you still win!")
    x = (c.get_rate('USD', 'EUR'))
    print(c.get_rate('USD', 'EUR'))
    print(x - 1)
    print(x + 1)
    y = float(input("What is the rate of USD to EUR? "))
    print(y)

    if x + 1 > y > x - 1 or y == x:
        print("You Got it right! Well Done!")
        print(f"Your number was {y} but the Rate is {x}")
    else:
        print("Bop, You got it wrong... Try Next Time!")


def Start_Currency_Game2():
    Print_Currency_Welcome()
    sleep(1.5)
    print("Difficulty 1 - you can get wrong between +0.5 or -0.5")
    print("Example: Your answer is 1.2 but the rate is 0.8 so you still win!")
    x = (c.get_rate('USD', 'GBP'))
    print(c.get_rate('USD', 'GBP'))
    print(x - 0.5)
    print(x + 0.5)
    y = float(input("What is the rate of USD to GBP? "))
    print(y)

    if x + 0.5 > y > x - 0.5 or y == x:
        print("You Got it right! Well Done!")
    else:
        print("Bop, You got it wrong... Try Next Time!")


def Start_Currency_Game3():
    Print_Currency_Welcome()
    sleep(1.5)
    print("Difficulty 1 - you can get wrong between +0.2 or -0.2")
    print("Example: Your answer is 1 but the rate is 0.8 so you still win!")
    x = (c.get_rate('USD', 'CAD'))
    print(c.get_rate('USD', 'CAD'))
    print(x - 0.2)
    print(x + 0.2)
    y = float(input("What is the rate of USD to CAD? "))
    print(y)

    if x + 0.2 > y > x - 0.2 or y == x:
        print("You Got it right! Well Done!")
    else:
        print("Bop, You got it wrong... Try Next Time!")
