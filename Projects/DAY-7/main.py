import random
from hangman_words import  word_list
from hangman_art import  *
word_list = word_list;
print(logo)
chosen_word = random.choice(word_list)

length = len(chosen_word)
lives = 6
end_of_game = False
display = []

for _ in chosen_word :
    display += ["_"]

#Ask for the letter and make it to lower case
#while chosen_word != ''.join(display):
while not end_of_game:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
        continue
    for i in range(length):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in word.You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose!!")
    if ''.join(display)  == chosen_word:
        end_of_game = True
        print("You Win!!")
