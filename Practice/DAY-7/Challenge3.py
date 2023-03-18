
import random

word_list = ["ardvark","baboon","camel"]

#Randomly chose a word from the list
chosen_word = random.choice(word_list)
print(f"Chosen word if {chosen_word}")
length = len(chosen_word)

display = []
for _ in chosen_word :
    display += ["_"]

#Ask for the letter and make it to lower case
#while chosen_word != ''.join(display):
while "_" in display:
    guess = input("Guess a letter : ").lower()
    for i in range(length):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
    print(display)
print("Win!!")