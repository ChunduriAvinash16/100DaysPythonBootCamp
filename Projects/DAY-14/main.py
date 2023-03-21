import random

from art import logo, vs
from game_data import data

score = 0

def generate_description(data):
    return f"{data['name']}, a {data['description']}, from {data['country']}."


def get_data():
    details = random.choice(data)
    name = generate_description(details)
    followerCount = details['follower_count']
    return name, followerCount


def checking_condition(followers_check, followerCountOfA, followerCountOfB):
    if (followers_check == 'A' and followerCountOfA > followerCountOfB) or \
            (followers_check == 'B' and followerCountOfB > followerCountOfA):
        global score
        score += 1
    elif followers_check in 'AB':
        return True
    else:
        print("Wrong Choice")
        return True


def game():
    isGameOver = False
    print(logo)
    while not isGameOver:
        nameA, followerCountOfA = get_data()
        if score != 0:
            print(f"You're right! Current Score: {score}.")
        print(f"Compare A: {nameA}")
        print(vs)
        nameB, followerCountOfB = get_data()
        print(f"Aganist B: {nameB}")
        followers_check = input("Who has more more followers? Type 'A' or 'B':")
        isGameOver = checking_condition(followers_check,followerCountOfA,followerCountOfB)
    print(f"Sorry, that's wrong. Final Score: {score}")


game()
