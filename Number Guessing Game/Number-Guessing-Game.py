#import library
import random
import time
import sys


def WeclomMssage():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
def game():
    chances = 0
    chances1 = 0
    number = random.randint(1,100)
    global Input1
    Input1 = int(input("Enter your choice: "))
    if Input1 == 1:
        print("Great! You have selected the Easy difficulty level.\nLet's start the game!")
        chances = 10
    elif Input1 == 2:
        print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
        chances = 5
    elif Input1 == 3:
        print("Great! You have selected the Hard difficulty level.\nLet's start the game!")
        chances = 3
    else:
        print("invalid input")
        sys.exit(1)
    time1 = time.time()
    while chances > chances1:
        chances1 += 1
        guess = int(input("Enter your guess: "))
        if guess == number:
            time2 = time.time()
            elapsed_time = time2 - time1  # Total time in seconds
            # Convert to hours, minutes, and seconds
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            print(f"Congratulations! You guessed the correct number in {chances1} attempts.\nYou're Guessing time is : {hours} hours {minutes} minutes and {seconds} seconds .")
            agine = int(input("Do you want to play agin (1 for Yes , 2 for No)?:\n1.Yes\n2.No\nInput : "))
            if agine == 1:
                main()
            else:
                sys.exit(0)
        elif guess < number:
            print(f"Incorrect! The number is greater then {guess}\nYou have {chances - chances1} chances left.")
        elif guess > number:
            print(f"Incorrect! The number is less then {guess}\nYou have {chances - chances1} chances left..")
    else:
        print(f"You are out of chances, You have only {chances1} chance.")
        agine = int(input("Do you want to play agin (1 for Yes , 2 for No)?:\n1.Yes\n2.No\nInput : "))
        if agine == 1:
            main()
        else:
            sys.exit(0)
def main():
    WeclomMssage()
    game()
main()