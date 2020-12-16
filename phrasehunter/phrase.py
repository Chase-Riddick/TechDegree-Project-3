class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase


    def display(self, guesses):
        """ Diplays the amount of the active phrase already completed/ indentified by the user."""
        for letter in self.phrase:
            if letter == " ":
                print(" ", end=" ")
            else:
                matches_guess = False
                for guess in guesses:
                    if guess == letter:
                        print(f"{letter}", end=" ")
                        matches_guess = True
                if matches_guess == False:
                    print("_", end=" ")


    def check_phrase(self, guess):
        """ If user guess is in phrase, it returns a true value."""
        if guess in self.phrase:
            return True


    def check_complete(self, guesses):
        """ Checks whether all the letters in the phrase are contained in the guess list; 
        if it does, it returns true, otherwise false."""
        for letter in self.phrase:
            if letter not in guesses:
                return False 
        return True