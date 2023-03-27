import random
from turtle import Turtle, Screen

timmy = Turtle()


def draw_shape(num_side):
    for _ in range(num_side):
        timmy.forward(100)
        timmy.right(360 // i)


colors = ["royal blue", "blue", "medium turquoise", "olive drab", "dark goldenrod"]
for i in range(3, 11):
    timmy.pencolor(random.choice(colors))
    draw_shape(i)

Screen().exitonclick()
