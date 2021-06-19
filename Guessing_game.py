import random
counter = 0
new_game = True
score_list = []


def current_scoring():
    if len(score_list) == 0:
        print("No scores recorded yet.")
    if len(score_list) > 0:
        print()
        print("...these are the existing scores: ")
        for score in score_list:
            print("* " + str(score))
        print()


print("------------------------------------------")
print("-                                        -")
print("-    Random Number Guessing Game 1-20    -")
print("-  Guess a number and we will tell you   -")
print("-    if it's too high or too low.  We    -")
print("-  will tell you how guesses you made.   -")
print("-                                        -")
print("------------------------------------------")
print()

while new_game:
    current_scoring()
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
                    print("You GOT it! Random number is {} and you guessed {} times".format(
                        num, counter))
                    score_list.append(counter)
                    if len(score_list) == 1:
                        print("Your score of {} is the best score, but it's also the only score.".format(
                            counter))
                        print()
                    if len(score_list) > 1:
                        print()
    play_again = True
    while play_again:
        print("Would you like to play again? (y/n)")
        play = input("> ")
        if (play.lower() == "y") or (play.lower() == "n"):
            if (play.lower() == "y"):
                new_game = True
                counter = 0
                play_again = False
            if (play.lower() == "n"):
                new_game = False
                play_again = False
        else:
            play_again = True
print("End game.")
print()
current_scoring()
print()
