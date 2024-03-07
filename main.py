from time import sleep
from better_input import better_input
from functions import *

# items, variables, whatever
character_name = ""  # this is better than global
items = []


# Character Creator
def creator():
    name = input("What would you like to name your character? ")
    x = better_input("Your character is named: " + name + ". Do you wish to continue? [y] [n] ", ["y", "y", "n", "n"])
    if match_from_array(x, ['y', 'y']):
        return name
    elif match_from_array(x, ['n', 'n']):
        return creator()


# the first part of the game
def intro():
    print(
        character_name + ' wakes up in a confined, medium sized room. All that goes through their head is just how did they get there?')
    sleep(3)
    x = better_input(
        "That doesn't matter, your goal is to help them get out of this weird area they are not famillar this, do you wish to cooperate? [y] [n] ",
        ["y", "y", "n", "n"])
    if match_from_array(x, ['y', 'y']):
        main()
        clean()
    elif match_from_array(x, ['n', 'n']):
        print("So you leave ", +character_name + " to die, interesting.")


def main(wrenchevent=True):
    print(
        character_name + " stands in the center of the room, all thats around them is a vent, a bed, a desk with a laptop on it and a steel door with a keypad on it, what does " + character_name + " do?")
    x = better_input("Check Vent [1] Check Desk [2] Check Door [3] Check Bed [4] ", ["1", "2", "3", "4"])
    if match_from_array(x, ['1', '1']):  # "Check Vent"
        print("Vent")
    elif match_from_array(x, ['2', '2']):  # "Check Desk"
        x = better_input(
            character_name + " is at the desk, theres a laptop with power on and a few drawers, what do they do? [1] Check Laptop [2] Check the drawers [3] Go back ",
            ["1", "2", "3"])
        if match_from_array(x, ['1', '1']):
            print("test")
        elif match_from_array(x, ['2', '2']):
            x = better_input(
                "They open the drawer and find a wrench, the wrench looks rusty and seems like it can be used for something, does " + character_name + " want to take the wrench? [y] [n] ",
                ['y', 'y', 'n', 'n'])
            if match_from_array(x, ['y', 'y']):
                print("hi")
                wrenchevent = False
                print(wrenchevent)
                main()
            if not wrenchevent:
                print("bye")
                main()





        elif match_from_array(x, ['3', '3']):
            main()
    elif match_from_array(x, ['3', '3']):  # "Check Door"
        print("Door")
    elif match_from_array(x, ['4', '4']):  # "Check Bed"
        print("Bed")


def test():
    """"
    used for testing my input function
    """
    x = better_input("hello? [hi] [no]", ["hi", "no"])
    print(x)


# test()


character_name = creator()
intro()
