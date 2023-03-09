print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

divertion = input("You're at the cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if divertion == "left":
    swin_or_wait = input(
        'you come to the lake. There is an island in the middle of lake. Type "wait" to wait for a boat. Type "swim"'
        ' to swim across\n').lower()
    if swin_or_wait == "wait":
        door = input(
            "You arrive at island unharmed.There is a house with 3 doors.One red,one yellow and one blue. Which colour do you choose?\n").lower()
        if door=="red" or door=="blue":
            print("Game Over.")
        elif door=="yellow":
            print("You Win!")
        else:
            print("Your Choice doesn't exist, Game Over!")
    else:
        print("Game Over.")
else:
    print("Game Over.")

