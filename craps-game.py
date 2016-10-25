'''
Craps Game
'''

import random

def diceRoll():
    pause = input("Press <Enter> to roll the dice!")
    roll =  random.randrange(6) + 1 + random.randrange(6) + 1
    print("You rolled a: {}".format(roll))
    return roll

def main():
    response = input("Do you want to play the Craps Game? y or n: ")
    if response == "y":
        instructions = input("Do you need instructions? y or n: ")
        if instructions == "y":
            print("Here are the instructions:")
    while response == 'y':
        firstRoll = diceRoll()
        if firstRoll == 7 or firstRoll == 11:
            print("You won!")
        elif firstRoll == 2 or firstRoll == 3 or firstRoll == 12:
            print("You lost!")
        else:
            print("We're going to try and roll the point!")
            point = firstRoll
            newRoll= diceRoll()
            while newRoll != point and newRoll != 7:
                newRoll = diceRoll()
            if newRoll == point:
                print("You lost!")
            else:
                print("You lost!")
        response = input("Do you want to play again? y or n: ")
    print("Okay, see you next time!")

if __name__ == "__main__":
    main()