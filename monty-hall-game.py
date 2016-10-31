'''
Monty Hall Game
'''

import random

def main():

    prizes = ["goat", "goat", "car"]
    doors = []
    while(len(prizes)) > 0:
        prizeNumber = random.randrange(len(prizes))
        doors.append(prizes.pop(prizeNumber))
        print(doors)

    choice1 = eval(input("Choose a door 1 - 3: "))

    print("Before we show you your prize, let's show you")
    print("another door...")
    while(True):
        randDoor = random.randrange(len(doors))
        if doors[randDoor] != "car" and choice1 - 1 != randDoor:
            break
    print("Take a look at {}".format(randDoor + 1))
    print(doors[randDoor])

    choice2 = eval(input("This is your last chance! Which door? "))
    print("You get a...{}".format(doors[choice2 - 1]))

main()