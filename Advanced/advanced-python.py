# This python script will teach you some advanced concepts in Python programming.
# We will be making  a simple game of rock paper scissors using the random module and if-else statements. 

import random

def get_user_choice():
    """Asks user for their choice and returns it as an integer."""
    while True:
        try:
            user_input = int(input("Enter your choice (1 - Rock, 2 - Paper, 3 - Scissors): "))
            if user_input < 1 or user_input > 3:
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")

def get_computer_choice():
    """Generates a random number between 1 and 3 and returns it as an integer."""
    return random.randint(1, 3)

def check_winner(user_choice, computer_choice):
    """Checks who won the game based on the given choices and prints out the result."""
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 1 and computer_choice == 3 or user_choice == 3 and computer_choice == 1:
        print("Rock crushes scissors! You win this round.")
    elif user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 2:
        print("Paper covers rock! You win this round.")
    else:
        print("Scissors cut paper! The computer wins this round.")

def play_game():
    """Plays one round of the game and asks the user to play again."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("\nYour choice is...\t\tThe computer's choice is...")
    print(f"You chose {['Rock', 'Paper', 'Scissors']}")
    print([f"{['Rock', 'Paper', 'Scissors'][computer_choice - 1]}\n"])
    check_winner(user_choice, computer_choice)
    play_again = input("\nDo you want to play again? (yes/no)\n").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing!")