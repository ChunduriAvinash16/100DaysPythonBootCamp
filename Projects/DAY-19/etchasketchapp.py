import random
from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(random.randint(10, 100))


def move_backward():
    timmy.backward(random.randint(10, 100))


def turn_left():
    timmy.setheading(timmy.heading()+10)
    # timmy.left(10)

def turn_right():
    timmy.setheading(timmy.heading()-10)
    # timmy.right(-10)

def clear():
    timmy.reset()

screen = Screen()
screen.listen()
screen.mode("standard")
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()
