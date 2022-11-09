import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def print_intro(enemy, weapon):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {enemy} is somewhere "
                "around here, and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                f"(but not very effective) {weapon}.")


def make_choice(options):
    user_choice = input(f"Please enter {options[0]} or {options[1]}.\n")
    if options[0] in user_choice or options[1] in user_choice:
        return user_choice
    else:
        make_choice(options)


def fight(enemy, weapon):
    if weapon != "Sword of Ogoroth":
        print_pause("You do your best...")
        print_pause(f"but your {weapon} is no match for the {enemy}.")
        print_pause("You have been defeated!")
    elif weapon == "Sword of Ogoroth":
        print_pause(f"As the {enemy} moves to attack, "
                    "you unsheath your new sword.")
        print_pause(f"The {weapon} shines brightly in your hand as "
                    "you brace yourself for the attack.")
        print_pause(f"But the {enemy} takes one look at "
                    "your shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {enemy}."
                    "You are victorious!")

def enter_cave(enemy, weapon):
    print_pause("You peer cautiously into the cave.")
    if weapon != "Sword of Ogoroth":
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old "
                    f"{weapon} and take the sword with you.")
        weapon = "Sword of Ogoroth"
    else:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
        enter_field(enemy, weapon)

    print_pause("You walk back out to the field.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    options = ["1", "2"]
    user_choice = make_choice(options)
    if "1" in user_choice:
        enter_house(enemy, weapon)
    elif "2" in user_choice:
        enter_cave(enemy, weapon)


def enter_field(enemy, weapon):
    print_pause("Enter 1 to knock the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n")
    options = ["1", "2"]
    user_choice = make_choice(options)
    if "1" in user_choice:
        enter_house(enemy, weapon)
    elif "2" in user_choice:
        enter_cave(enemy, weapon)


def enter_house(enemy, weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                f"what with only having a tiny {weapon}.")
    print_pause("Would you like to (1) fight or (2) run away?")
    options = ["1", "2"]
    user_choice = make_choice(options)
    if "1" in user_choice:
        fight(enemy, weapon)
    elif "2" in user_choice:
        print_pause("You run back into the field. "
                    "Luckily, you don't seem to have been followed.")
        enter_field(enemy, weapon)


def print_outro():
    print_pause("Would you like to play again?")
    options = ["y", "n"]
    user_choice = make_choice(options)
    if "y" in user_choice:
        print_pause("Excellent! Restarting the game...")

    elif "n" in user_choice:
        print_pause("Thanks for playing! See you next time.")

    return user_choice[0]        


def main():

    weapons = ["dagger", "sword", "axe", "bat"]
    enemies = ["pirate", "troll", "zombie", "werewolf"]

    play_again = "y"
    while play_again == "y":
        weapon = random.choice(weapons)
        enemy = random.choice(enemies)
        print_intro(enemy, weapon)
        enter_field(enemy, weapon)
        play_again = print_outro()


if __name__ == "__main__":
    main()
