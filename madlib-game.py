'''
Madlib Game in Python
'''

print("Let's play Madlibs!")

name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
food = input("Enter a food (plural): ")
noun2 = input("Enter a noun (plural): ")
verb = input("Enter a verb ending in 'ed': ")
noun3 = input("Enter another noun: ")

print("Come on over to {}’s Pizza Parlor\n"
      "where you can enjoy your favorite {}-dish pizza`s.\n"
      "You can try our famous {}-lovers pizza, \n"
      "or select from our list of {} toppings, \n"
      "including delicious {}, {}, and many more. \n"
      "Our crusts are hand-{} and basted in {} to make \n"
      "them seem more Hand-made.".format(name, adjective1, noun1,
                                         adjective2, food, noun2,
                                         verb, noun3))
