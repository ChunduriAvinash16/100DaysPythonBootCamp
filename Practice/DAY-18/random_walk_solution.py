import random
from turtle import Turtle,Screen

timmy = Turtle()
directions = [0,90,180,270]
colors = ["royal blue", "blue", "medium turquoise", "olive drab", "dark goldenrod","olive","deep pink","dark salmon"]
timmy.pensize(10)
timmy.speed("fastest")
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

Screen().exitonclick()