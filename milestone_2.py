
import random
word_list=['apple', 'banana', 'orange', 'kiwi', 'strawberry']

print(word_list)


word= random.choice(word_list)      #random is module(package) and choice is function

print(word)

guess = input('enter the guess')
if len(guess)== 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")    





