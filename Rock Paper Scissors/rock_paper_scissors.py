import sys
import random
from enum import Enum

class RockPaperScissors(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    QUIT = 4

print()
while True:
    userinput = input("Enter "
                       "\n1 for Rock"
                       "\n2 for Paper"
                       "\n3 for Scissors"
                       "\n4 to Quit"
                       "\n\n")


    user_input = int(userinput)

    if user_input < 1 or user_input > 4:
        print("Invalid input. "
              "\nPlease enter 1, 2, 3, or 4")


    if user_input == 4:
        print("You choose to quit the game")
        sys.exit()



    computerchoice = random.choice([1, 2, 3])
    computer_choice = int(computerchoice)

    print()

    print("You choose:", str(RockPaperScissors(user_input).name))
    print("Computer choose:", str(RockPaperScissors(computer_choice).name))


    if user_input == 1 and computer_choice == 3:
        print("You Win!")
    elif user_input == 2 and computer_choice == 1:
        print("You Win!")
    elif user_input == 3 and computer_choice == 2:
        print("You Win!")
    elif user_input == computer_choice:
        print("Tie!")

    else:
        print("Computer Wins!")

    play_again = input("\nDo you want to play again?"
                       "\n1 for Yes"
                       "\n2 for No"
                       "\n\n")

    if play_again != "1":
        print("You have choose to quit the game")
        break


