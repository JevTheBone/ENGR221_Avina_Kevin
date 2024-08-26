#
# Name: Kevin Avina-Gutierrez
# Lab1.py
# Description: Following Lab 01 assignment instructions after 4e.
# the goal is to play rock paper scissors.

import random          # imports the library named random

def rps():
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
    #first variable we assign#
    message = "Go gators!" 
    #Print statement to display -message- in the console.#
    print(message)

    user = input("Choose your weapon: ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock' and comp == 'scissors':
        print('Ha! I actually chose paper, which annihilates your rock.')
        print("Better luck next time...")

    elif user == 'rock' and comp == 'paper':
        print('I won! Your rock is dust!')
        print("Better luck next time...")
    
    elif user == 'rock' and comp == 'rock':
        print('Perhaps this makes us even... lets go again!')
   
    if user == 'scissors' and comp == 'paper':
        print('You win this time, lucky guess that is all!')
    
    elif user == 'scissors' and comp == 'rock':
        print('This was almost too easy!')
        print("Better luck next time...")

    elif user == 'scissors' and comp == 'scissors':
        print('Well played champ, let me get that rematch!')

    if user == 'paper' and comp == 'rock':
        print('You win this time, lucky guess that is all!')
    
    elif user == 'paper' and comp == 'scissors':
        print('This was almost too easy!')
        print("Better luck next time...")

    elif user == 'paper' and comp == 'paper':
        print('Well played champ, let me get that rematch!')

rps()
