from game import Game
from phrase import Phrase
import sys

def print_continue_playing_prompt():
    """ Prints prompts asking user whether they would like to continue playing game."""
    print("\n\n\n----- Would you like to continue playing? -----")
    print("Enter 'C' if you'd like to continue, and play again.")
    print("Enter 'E' if you would like to finish playing, and exit the application.")


def  user_input():
    """Collects users input """
    user_input = input("What would you like to do? >>> ")
    return user_input


def constrain_user_input(input_function):
    """ Constrains user_input to C (continue) or E (exit)."""
    input_value = input_function.upper()
    accepted_values = ["C","E"]
    accepted_values[0]
    accepted_values[1]
    
    if input_value != accepted_values[0] or input_value != accepted_values[1]:
        while input_value != accepted_values[0] and input_value != accepted_values[1]:
            print(f"Sorry, '{input_value}' isn't an accepted option. Please input 'C' or 'E' (Continue/ Exit)")
            input_value = user_input()

    return input_value


def proceed_or_exit_app(user_command_input):
    """ Runs user input, exiting if user inputs corresponding value."""
    user_command = user_command_input
    if user_command == "E":
        exit_app()
        

def exit_app():
    """ Completes exit of application."""
    print("\nThanks for taking the time to check out this application. \nHave a great day, and I'll hope to see you around here again soon.")
    print("Bye bye!")
    sys.exit()


if __name__ == "__main__":
    
    while True: 
        game_instance = Game()
        game_instance.run_game()
        print_continue_playing_prompt()
        user_command = constrain_user_input(user_input())
        proceed_or_exit_app(user_command)