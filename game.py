# Write your code here
import random
import sys


def add_score(username, names):
    index = 0
    for name in names:
        name = name.rstrip()
        if name.split()[0] == username:
            score = int(name.split()[1]) + 100
            output = f"{username} {score}\n"
            names[index] = output
        index += 1


def draw_score(username, names):
    index = 0
    for name in names:
        name = name.rstrip()
        if name.split()[0] == username:
            score = int(name.split()[1]) + 50
            output = f"{username} {score}\n"
            names[index] = output
    index += 1


if __name__ == "__main__":

    # Declare winning combinations
    # Key beats Values
    winning = {
        "rock": ["sponge", "wolf", "tree", "human", "snake", "scissors", "fire"],
        "gun": ["wolf", "tree", "human", "snake", "scissors", "fire", "rock"],
        "lightning": ["tree", "human", "snake", "scissors", "fire", "rock", "gun"],
        "devil": ["human", "snake", "scissors", "fire", "rock", "gun", "lightning"],
        "dragon": ["snake", "scissors", "fire", "rock", "gun", "lightning", "devil"],
        "water": ["scissors", "fire", "rock", "gun", "lightning", "devil", "dragon"],
        "air": ["fire", "rock", "gun", "lightning", "devil", "dragon", "water"],
        "paper": ["rock", "gun", "lightning", "devil", "dragon", "water", "air"],
        "sponge": ["gun", "lightning", "devil", "dragon", "water", "air", "paper"],
        "wolf": ["lightning", "devil", "dragon", "water", "air", "paper", "sponge"],
        "tree": ["devil", "dragon", "water", "air", "paper", "sponge", "wolf"],
        "human": ["dragon", "water", "air", "paper", "sponge", "wolf", "tree"],
        "snake": ["water", "air", "paper", "sponge", "wolf", "tree", "human"],
        "scissors": ["air", "paper", "sponge", "wolf", "tree", "human", "snake"],
        "fire": ["paper", "sponge", "wolf", "tree", "human", "snake", "scissor"],
    }

    # Output a line Enter your name: . Note that the user should enter his/her name on
    # the same line (not the one following the output!)
    username = input("Enter your name: ")

    # Read input specifying the user's name and output a new line Hello, <name>
    print(f"Hello, {username}")

    # Read a file named rating.txt and check if there's a record for the user with the
    # same name; if yes, use the score specified in the rating.txt for this user as a
    # starting point for calculating the score in the current game.
    # If no, start counting user's score from 0.
    with open("rating.txt", "r") as file:  # Open text file and
        names = file.readlines()  # pass values to an array

    valid_choices = []

    # Read input specifying the list of options that will be used for playing
    # the game (options are separated by comma).
    # If the input is an empty line, play with default options.
    choices = input()
    if choices == "":
        valid_choices = ["rock", "paper", "scissors"]
        print(f"Choices: {valid_choices}")
    else:
        valid_choices = choices.split(",")
        print(f"Choices: {valid_choices}")

    # Output a line Okay, let's start
    print("Okay, let's start")

    while True:
        # Read user's input
        while True:
            user_input = input()
            if (
                (user_input in valid_choices)
                or (user_input == "!rating")
                or (user_input == "!exit")
            ):
                break
            else:
                print("Invalid input")

        # If the input is the name of the option, then:
        # Pick a random option
        computer = valid_choices
        random.shuffle(computer)
        comp_choice = computer[0]

        # Output a line with the result of the game in the following
        # format (<option> is the name of the option chosen by the program):

        if user_input == "!rating":
            for name in names:
                name = name.rstrip()
                if name.split()[0] == username:
                    score = name.split()[1]
                    print(f"Your rating: {score}")
        elif user_input == "!exit":
            print("Bye!")
            with open("rating.txt", "w") as file:
                for name in names:
                    file.write(name + "\n")
            sys.exit(0)
        elif comp_choice == user_input:  # Draw -> There is a draw (<option>)
            print(f"There is a draw ({user_input})")
            draw_score(username, names)
        elif (
            comp_choice in winning[user_input]
        ):  # Win -> Well done. The computer chose <option> and failed
            print(f"Well done. The computer chose {comp_choice} and failed")
            add_score(username, names)
        elif (
            comp_choice not in winning[user_input]
        ):  # Lose -> Sorry, but the computer chose <option>
            print(f"Sorry, but the computer chose {comp_choice}")
