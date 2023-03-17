import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
if user_choice > 2 or user_choice < 0:
 print("Invalid Input!!!")
else:
 print(images[user_choice])
 Computer_Choice = random.randint(0,2)
 print(f"Computer chose: {Computer_Choice}")

 print(images[Computer_Choice])
 if user_choice==0 and Computer_Choice == 2:
  print("You win")
 elif user_choice==2 and Computer_Choice==0:
  print("You lose")
 elif Computer_Choice > user_choice:
  print("You lose")
 elif user_choice > Computer_Choice:
  print("You Win")
 elif Computer_Choice == user_choice:
  print("It's Draw!!!!!")

