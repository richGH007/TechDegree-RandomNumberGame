# """
# Python Web Development Techdegree
# Project 1 - Number Guessing Game
# --------------------------------

# For this first project we will be using Workspaces.

# NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> #Download Workspace in the file menu after you fork the snapshot of this workspace.

# """

#import random


# def start_game():
#    """Psuedo-code Hints
#
#    When the program starts, we want to:
#    ------------------------------------
#    1. Display an intro/welcome message to the player.
#    2. Store a random number as the answer/solution.
#    3. Continuously prompt the player for a guess.
#      a. If the guess greater than the solution, display to the player "It's lower".
#      b. If the guess is less than the solution, display to the player "It's higher".
#
#    4. Once the guess is correct, stop looping, inform the user they "Got it"
#         and show how many attempts it took them to get the correct number.
#    5. Let the player know the game is ending, or something that indicates the game is over.
#
#    ( You can add more features/enhancements if you'd like to. )
#    """
#    # write your code inside this function.

# Kick off the program by calling the start_game function.
# start_game()
import random
counter = 0
new_game = True

print("------------------------------------------")
print("-                                        -")
print("-    Random Number Guessing Game 1-20    -")
print("-  Guess a number and we will tell you   -")
print("-    if it's too high or too low.  We    -")
print("-  will tell you how guesses you made.   -")
print("-                                        -")
print("------------------------------------------")

while new_game:
    num = random.randint(1, 20)
    # print(num)
    guess_NOTvalid = True
    while guess_NOTvalid:
        print()
        print("Guess a number between 1 and 20.")
        try:
            guessed_num = int(input("> "))
        except ValueError:
            print("Oh no! That is not a valid number.  Try again...")
            guess_NOTvalid = True
        else:
            if (guessed_num <= 0) or (guessed_num >= 21):
                print("Oh no! That is not a valid number.  Try again...")
                guess_NOTvalid = True
            else:
                if guessed_num < num:
                    print("It's higher.")
                    counter += 1
                    guess_NOTvalid = True
                if guessed_num > num:
                    print("It's lower.")
                    counter += 1
                    guess_NOTvalid = True
                if guessed_num == num:
                    counter += 1
                    guess_NOTvalid = False
                    print("Random number is {} and you guessed {} times".format(
                        num, counter))

        # Ask the player if (s)he wants to try again.

        new_game = False
