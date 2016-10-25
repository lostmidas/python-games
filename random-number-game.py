'''
Random Number Game
'''

import random

def main():
# Initialze the program
    print("Guess a number between 1 and 100.")
#randomNumber = int(35) for debugging only
    randomNumber = int(random.randint(1,100))
# Flag variable to see if they guessed it
    found = False
# Run through the guessing process

    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == randomNumber:
            print("You got it!")
            found = True
        elif userGuess > randomNumber:
            print("Guess lower!")
        else:
            print("Guess higher!")

    #Print congratulations and goodbye
    print("Thanks for playing our game!")

main()
