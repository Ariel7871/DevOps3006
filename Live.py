import random
import os
from time import sleep
from MemoryGame import Memory_Game
from GuessGame import Guess_Game
from Currency_Roulette import Currency_Roulette
from Score import add_score

name = input("enter your name: ")


def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).')
    print("Here you can find many cool games to play.")


welcome(name)



def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount like USD in ILS")



load_game()

game = int(input("Please select the number of the game you want to play: "))

if game == 1:
    Memory_Game()


elif game == 2:
    Guess_Game()

elif game == 3:
    Currency_Roulette()

else:
    print("Please choose 1 to 3 only")

