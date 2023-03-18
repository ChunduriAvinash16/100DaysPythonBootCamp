import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark","baboon","camel"]

#Randomly chose a word from the list
chosen_word = random.choice(word_list)
# print(f"Chosen word if {chosen_word}")
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
    for i in range(length):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
            break
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose!!")
    if ''.join(display)  == chosen_word:
        end_of_game = True
        print("You Win!!")
