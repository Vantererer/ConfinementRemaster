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
    x = better_input(
        "That doesn't matter, your goal is to help them get out of this weird area they are not famillar this, do you wish to cooperate? [y] [n] ",
        ["y", "y", "n", "n"])
    if match_from_array(x, ['y', 'y']):
        main()
        clean()
    elif match_from_array(x, ['n', 'n']):
        print("So you leave ", +character_name + " to die, interesting.")


def main(draw = {'isEmpty': False}):

    print(
        character_name + " stands in the center of the room, all thats around them is a vent, a bed, a desk with a laptop on it and a steel door with a keypad on it, what does " + character_name + " do?")
    x = better_input("Check Vent [1] Check Desk [2] Check Door [3] Check Bed [4] Check Items [5] ", ["1", "2", "3", "4", "5"])
    if match_from_array(x, ['1', '1']):  # "Check Vent"
        print("They walk to the vent and look inside, theres a orange crowbar inside of there, perhaps they could open the vent with a tool.")
        wait(2)
    if 'Wrench' in items:
        print("t")
        main()

    elif match_from_array(x, ['2', '2']):  # "Check Desk"
        x = better_input(
            character_name + " is at the desk, theres a laptop with power on and a few drawers, what do they do? [1] Check Laptop [2] Check the drawers [3] Go back ",
            ["1", "2", "3"])
        if match_from_array(x, ['1', '1']):
            print("t")
        elif match_from_array(x, ['2', '2']):
            x = better_input(
                "There is one drawer that can be opened, the rest don't budge. Does " + character_name + " want to open it? [y] [n] ",
                ['y', 'y', 'n', 'n'])
            if match_from_array(x, ['y', 'y']):
                if not draw["isEmpty"]:
                    print(character_name+" finds a wrench and they take it, perhaps they'll use it for something.")
                    items.append("Wrench")
                    draw["isEmpty"] = True
                    main()
                else:
                    print("The drawers are empty now, no need to interact with them or look more.")
                if not draw["isEmpty"]:
                    print(character_name+" takes the wrench, perhaps they'll use it for something.")
                    draw["isEmpty"] = True
                    main()
                else:
                    main()

                if not draw["isEmpty"]:
                    print(character_name+" finds a wrench and they take it, perhaps they'll use it for something.")
                    draw["isEmpty"] = True
                    main()
                else:
                    main()






    elif match_from_array(x, ['3', '3']):  # "Check Door"
        print("Door")
    elif match_from_array(x, ['4', '4']):  # "Check Bed"
        print("Bed")
    elif match_from_array(x, ['5','5']):   # 'Check Items'
        print(items)
        main()


def test():
    """"
    used for testing my input function
    """
    x = better_input("hello? [hi] [no]", ["hi", "no"])
    print(x)


# test()


character_name = creator()
intro()
