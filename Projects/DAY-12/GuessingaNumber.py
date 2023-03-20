import random
from art import  logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def guess_number(rand_number,chances):
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess:"))
        if guessed_number > rand_number:
            print("Too high.")
            print("Guess Again.")
        elif guessed_number < rand_number:
            print("Too Low.")
            print("Guess Again.")
        else:
            print(f"You got it! The answer was {rand_number}")
            return
        chances -= 1

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")
    rand_number = random.randint(1,100)
    # print(rand_number)
    difficulty_level = input("Choose a difficulty.Type 'easy' or 'hard': ")

    if difficulty_level == 'easy':
        guess_number(rand_number,EASY_LEVEL_TURNS)
    elif difficulty_level == 'hard':
        guess_number(rand_number,HARD_LEVEL_TURNS)

game()