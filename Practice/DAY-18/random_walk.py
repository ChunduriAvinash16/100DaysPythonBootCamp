import random
from turtle import Turtle, Screen

timmy = Turtle()


def generate_random():
    choice = random.choice([1, 2, 3])
    if choice == 1:
        timmy.forward(25)
    elif choice == 2:
        timmy.right(90)
        timmy.forward(25)
    else:
        timmy.left(90)
        timmy.forward(25)


colors = ["royal blue", "blue", "medium turquoise", "olive drab", "dark goldenrod","olive","deep pink","dark salmon"]
count = 100
print("Started")
while count > 0:
    print("Inside")
    timmy.pensize(10)
    timmy.pencolor(random.choice(colors))
    generate_random()
    timmy.speed(10)
    count -= 1
Screen().exitonclick()
