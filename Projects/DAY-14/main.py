import random

from art import logo, vs
from game_data import data


def generate_description(data):
    return f"{data['name']}, a {data['description']}, from {data['country']}."


def get_data():
    details = random.choice(data)
    name = generate_description(details)
    followerCount = details['follower_count']
    return name, followerCount


def checking_condition(followers_check, followerCountOfA, followerCountOfB):
    if followerCountOfA > followerCountOfB:
        return followers_check == 'A'
    else:
        return followers_check == 'B'


def game():
    score = 0
    isGameOver = False
    print(logo)
    while not isGameOver:
        nameA, followerCountOfA = get_data()
        nameB, followerCountOfB = get_data()
        print(f"Compare A: {nameA}")
        print(vs)
        print(f"Aganist B: {nameB}")
        followers_check = input("Who has more more followers? Type 'A' or 'B':")
        isCheck = checking_condition(followers_check, followerCountOfA, followerCountOfB)

        if isCheck:
            score += 1
            print(f"You're right! Current Score: {score}.")
        else:
            isGameOver = True
            print(f"Sorry, that's wrong. Final Score: {score}")


game()
