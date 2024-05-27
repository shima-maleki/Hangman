import random


word_list = ['apple', 'banana', 'orange', 'kiwi', 'strawberry']

class Hangman:
    def __init__(self, word_list,  num_lives= 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed= ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses =[]


    def check_guess(self, guess ):
        print(self.word)
        guess= guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i,letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
            self.num_letters-=1  

        else:
            self.num_lives-=1
            print( f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):  
        while True:
            guess = input('guess a letter :')
            if not guess.isalpha() and len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.") 

            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            if game.num_lives != 0 and game.num_letters <= 0:
                print('Congratulations. You won the game!')
                break  

play_game(word_list)




   
      

''' 

Next, check if the num_letters is greater than 0. In this case, you would want to continue the game, so you need to call the ask_for_input method.
If the num_lives is not 0 and the num_letters is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'
Step 2:
Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.


'''