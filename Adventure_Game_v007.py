import time
import random


def print_pause(message_to_print=list()):
    print(''.join(message_to_print))
    time.sleep(1)


# Default intro
def intro():
    print_pause(["You find yourself in a peaceful meadow."])
    print_pause(["You have a trusty, (but not very good) dagger."])
    print_pause(["You see both a dark cave and a cute house."])
    print_pause(["Which way do you want to go?"])

# Cave choice
def cave(items):
    newweapons = (['Sword of Souls', 'Hammer of Diddling', 'Axe of Fragility'])
    weapon = (random.choice(newweapons))

    for weapon in items:
        if weapon in items:
            print_pause(["You already searched the cave and there is nothing left!"])
            print_pause(["You better go back and check on what's in that house."])
            adventure_choice(items)

    else:
        print_pause(["You explore the cave with what little light there is."])
        print_pause(["After a few moments, you find something interesting."])
        items.append(weapon)
        print_pause(["You have found the ", weapon, "!"])
    print_pause(["You head back to the meadow."])
    adventure_choice(items)


# House choice
def house(items):
    print_pause(["You politely knock on the door to see who's inside."])
    enemies = ['Minotaur', 'Aunt Sally', 'Woff']
    monster = random.choice(enemies)
    print_pause(["An awful ", monster, " suddenly appears!"])

    for weapon in items:
        if weapon in items:
            print_pause(["The ", monster, " lunges towards you full force!"])
            print_pause(["Luckily, you have your new ", weapon, " handy."])
            print_pause(["With a few quick strikes you slay the ", monster, "!"])
            print_pause(["A hard fought battle! You are victorious!"])
            play_again()

    else:
        print_pause(["You slash with your dagger, but it is ineffective!"])
        print_pause(["You also don't have any other weapons!"])
        print_pause(["With one swoop you are toast."])
        print_pause(["GAME OVER"])
        play_again()

# Beginning of the Game
def adventure_choice(items):
    print_pause(["Please enter 1 or 2"])
    choice = input(
        "1. House\n"
        "2. Cave\n"
    )
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)
    else:
        print_pause(["Invalid Entry. Please enter 1 or 2"])
        return choice


# Restarts the game
def play_again():
    response = input(
        "Would you like to try again?\n"
        "Please say 'yes' or 'no'.\n")
    if "no" in response.lower():
        print_pause(["Better luck next time!"])
        quit()

    elif "yes" in response.lower():
        print_pause(["Once more, with feeling!"])
        play_game()

    else:
        print_pause(["Invalid entry, please say yes or no."])
        play_again()

# Main gameplay order
def play_game():
    items = []
    intro()
    adventure_choice(items)

play_game()
