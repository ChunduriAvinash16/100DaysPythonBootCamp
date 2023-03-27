import random
import turtle
from turtle import Turtle,Screen

timmy = Turtle()
turtle.colormode(255)
directions = [0,90,180,270]
def generate_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)


timmy.pensize(10)
timmy.speed("fastest")
for _ in range(200):
    timmy.pencolor(generate_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

Screen().exitonclick()