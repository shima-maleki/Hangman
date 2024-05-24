
import random
fruits_list=['apple', 'banana', 'orange', 'kiwi', 'strawberry']

print(fruits_list)


word= random.choice(fruits_list)      #random is module(package) and choice is function

print(word)

user_guess = input('enter the guess')
if len(user_guess)== 1 and user_guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")    





