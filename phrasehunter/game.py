from phrase import Phrase
import random
import sys
import string

START_MESSAGE = (
        "\n     ==============================\n"
        "        Welcome to Phrase Hunter\n"
        "     ==============================\n"
)

RULES = (
        "Guidelines:\n"
        " - Identify and complete the famous phrases by guessing its letters.\n"
        " - If you can complete the phrase before making 5 incorrect guesses, you win.\n"
        " - If you make 5 incorrect guesses, you lose.\n"
        " - You can only input individual letters that you've not previously guessed.\n"
        )

CONGRATULATORY_MESSAGES = [
            "Nice Job!", 
            "Woohoo, that's great!",
            "Not bad, not bad at all.",
            "Good one!"
            ]

ENCOURAGING_MESSAGES = [
            "Oh, that's too bad",
            "Oh no!",
            "Good try, but no dice.",
            "Bad luck!",
    ]

LOSE_MESSAGE = (
        "\n\n--------------  Unfortunately... YOU LOSE! -------------- \n"
        "... because you've made 5 incorrect guesses.\n\n"
        "You've managed to complete this much of the phrase:\n"
        )

WIN_MESSAGE = (
        "\n\n-------------- YOU WIN! --------------\n"
        "You've completed the phrase: \n"
        )


class Game():
    
    def __init__(self):
        self.guesses = [" "]
        self.phrases = [
            Phrase('May the Force be with you'),
            Phrase('All roads lead to Rome'),
            Phrase('Life is a box of chocolates'),
            Phrase('Words are wind'),
            Phrase('Winter is coming'),
        ]
        self.active_phrase = self.get_random_phrase()
        self.missed = 0
        self.guess_count = 0


    def run_game(self):
        """ The main method that starts the game, loops through rounds taking guesses, 
        displaying the phrase as completed already, and once the finish conditions are 
        met, then finishing the game. """
        self.print_start_message()
        self.print_rules()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            self.diplay_and_guess_prompt()
            self.process_guess()
        self.game_over()


    def print_start_message(self):
        print(START_MESSAGE)
        

    def print_rules(self):
        print(RULES)


    def get_random_phrase(self):
        return self.phrases[random.randint(0, 4)]


    def print_guess_number(self):
        print(f"\nGuess #{self.guess_count + 1}:\n")


    def print_number_of_incorrect_guesses(self):
        print(f"\nNumber of Incorrect Guesses: {self.missed}")


    def diplay_and_guess_prompt(self):
        """ Contains three methods that together print for each round the number of guesses, 
        incorrect guesses, the phrase as completed so far, and takes guess."""
        self.print_guess_number()
        self.active_phrase.display(self.guesses)
        self.print_number_of_incorrect_guesses()


    def get_guess(self):
        return input("\nInput Guess: What letter would you like to guess next? >>> ")


    def constrain_guess(self):
        """ Constains user guess to a single letter not already guessed."""
        user_guess_input = self.get_guess()
        while (user_guess_input not in string.ascii_letters) or (user_guess_input in self.guesses):
            print(f"\nSorry, '{user_guess_input}' isn't a valid option.")
            print(f"Please input a letter (a - z) that you haven't already guessed.\n")
            user_guess_input = self.get_guess()
        return user_guess_input


    def get_and_convert_guess_to_both_cases(self):
        """ Calls get_guess (within/alongside constrain guess), and converts guess to oher case."""
        user_guess = self.constrain_guess()
        user_guess_uppercase = user_guess.upper()
        user_guess_lowercase = user_guess.lower()
        return user_guess_uppercase, user_guess_lowercase


    def append_guesses_to_guess_list(self, uppercase_guess, lowercase_guess):
        """ Appends both cases of guess to guess list."""
        self.guesses.append(uppercase_guess)
        self.guesses.append(lowercase_guess)


    def get_random_congratulatory_message(self):
        """ Grabs a random congratulatory message to display in case of correct guess."""
        self.selected_congratulatory_message = CONGRATULATORY_MESSAGES[random.randint(0, 3)]
        return self.selected_congratulatory_message


    def get_random_encouraging_messages(self):
        """ Grabs a random encouraging message to display in case of incorrect guess."""
        self.selected_encouraging_messages = ENCOURAGING_MESSAGES[random.randint(0, 3)]
        return self.selected_encouraging_messages


    def respond_to_guess(self, uppercase_guess, lowercase_guess):
        """ Increases overall guess_count by one; and if guess (in either case)
        is correct, prints corrsponding message; if incorrect, the same and increases
        the missed count by one ."""
        uppercase_guess_in_phrase_bool = self.active_phrase.check_phrase(uppercase_guess)
        lowercase_guess_in_phrase_bool = self.active_phrase.check_phrase(lowercase_guess)
        print("Result:", end=" ")

        if uppercase_guess_in_phrase_bool or lowercase_guess_in_phrase_bool:
            congratulatory_message = self.get_random_congratulatory_message()
            print(f"{congratulatory_message}", end=" ")
            print("Your guess is correct!\n")
    
        else:
            encouraging_message = self.get_random_encouraging_messages()
            print(f"{encouraging_message}", end=" ")
            print("Your guess is incorrect.\n")
            self.missed += 1

        self.guess_count += 1


    def process_guess(self):
        """ This method packages together three other methods. It gets guess and converts the user guess to both cases,
         appends it to the guess list, and processes correct and incorrect guesses accordingly."""
        user_guess_uppercase, user_guess_lowercase = self.get_and_convert_guess_to_both_cases()
        self.append_guesses_to_guess_list(user_guess_uppercase, user_guess_lowercase)
        self.respond_to_guess(user_guess_uppercase,user_guess_lowercase)
    

    def game_over(self):
        """ In run-game method, this method is called after the main guessing loop is finished 
        to handle a win and loss correspondingly."""
        
        if self.missed == 5:
            print(LOSE_MESSAGE)
        
        else:
            print(WIN_MESSAGE)
        
        print("      ", end=" ")
        self.active_phrase.display(self.guesses)