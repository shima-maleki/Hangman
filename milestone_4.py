import random

class Hangman:
    """
    A class to represent the game Hangman.

    Attributes
    ----------
    word_list : list
        List of words from which the game selects one word randomly.
    num_lives : int, optional
        Number of lives a player has, default is 5.
    word : str
        The word to be guessed, chosen randomly from word_list.
    word_guessed : list
        A list to track the guessed letters of the word.
    num_letters : int
        The number of unique letters in the word that need to be guessed.
    list_of_guesses : list
        A list to keep track of the letters that have already been guessed.

    Methods
    -------
    check_guess(guess):
        Checks if the guessed letter is in the word and updates the game state.
    ask_for_input():
        Prompts the player to guess a letter and validates the input.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Constructs all the necessary attributes for the Hangman object.

        Parameters
        ----------
        word_list : list
            List of words from which the game selects one word randomly.
        num_lives : int, optional
            Number of lives a player has, default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state.

        Parameters
        ----------
        guess : str
            The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and validates the input.
        """
        while True:
            guess = input('guess a letter: ')
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break



      

