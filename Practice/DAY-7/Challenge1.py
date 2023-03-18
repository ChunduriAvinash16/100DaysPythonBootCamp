import random

word_list = ["ardvark","baboon","camel"]

#Randomly chose a word from the list
chosen_word = random.choice(word_list)

#Ask for the letter and make it to lower case
guess = input("Guess a letter : ").lower()

#Checking whether the gussed letter present in the randomly chosen word
for char in chosen_word:
    if guess == char:
        print("Right")
    else:
        print("Wrong")