
import random
fruits_list=['apple', 'banana', 'orange', 'kiwi', 'strawberry']

word= random.choice(fruits_list)      #random is module(package) and choice is function

while True:
    guess = input('guess a letter: ')
    if guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


if guess in word:
    print(f'Good guess! {guess} is in the word.')
else:
    print(f"Sorry, {guess} is not in the word. Try again.")    


