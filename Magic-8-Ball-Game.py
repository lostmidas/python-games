'''
Magic 8-Ball Game
'''

import random

class Magic_8_ball: # Capitalise class names
    '''
    The Magic_8_ball class defines Magic_8_ball objects
    '''
    def __init__(self): # Tell object about itself - what it needs to know about itself
        self.replies = ["Yes!", "Signs point to yes!", # Put in keyword 'self' before replies
                        "Reply hazy. Ask again later.",
                        "I don't think so!", ""
                        "Definitely not"
                        ]
        self.reply = ""
        self.shake()

    # Shake 'method' or 'mutator" = "Setters" for setting the value
    def shake(self):
        # The shake method mutuates the Magic_8_Ball object to set a new random reply.
        rand_value = int(random.random() * len(self.replies))  # The * operator references the number of 'replies,'
        # which may change over time if I want to add more
        self.reply = self.replies[rand_value]
    # "Getters" for getting the value
    def get_reply(self):
        return self.reply

def main():
    print("Magic 8 Ball predicts the future!")
    my_8_ball = Magic_8_ball()

    while True:
        # Have the user enter a question
        question = input("Enter a Yes/No question: ")

        my_8_ball.shake()
        print(my_8_ball.get_reply())

        # Reply with a random Yes/Maybe/No response
        print(replies[rand_value])

        # Ask if they want to try again
        go_again = input("Would you like to ask another question? ")
        # If first (lower-case) letter in the answer is n...
        if go_again[0].lower() == "n":
            break

    print("Goodbye!")

main()
