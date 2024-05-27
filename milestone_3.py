
import random

fruits_list=['apple', 'banana', 'orange', 'kiwi', 'strawberry']

word= random.choice(fruits_list)      #random is module(package) and choice is function

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f"Sorry, {guess} is not in the word. Try again.") 

def ask_for_input(): 
    while True:
        guess = input('guess a letter: ')
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") 

    check_guess(guess) 

if __name__ == "__main__":
    ask_for_input()
    
