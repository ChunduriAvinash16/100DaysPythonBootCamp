
import random

word_list = ["ardvark","baboon","camel"]

#Randomly chose a word from the list
chosen_word = random.choice(word_list)
print(f"Chosen word if {chosen_word}")
length = len(chosen_word)

#Ask for the letter and make it to lower case
guess = input("Guess a letter : ").lower()

display = []
for _ in chosen_word :
    display += ["_"]
# display = ["_"] * length

#Checking whether the gussed letter present in the randomly chosen word
for i in range(length):
    if guess == chosen_word[i]:
        display[i] = chosen_word[i]
print(display)