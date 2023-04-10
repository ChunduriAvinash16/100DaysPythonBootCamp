from turtle import Turtle,Screen


def forward_10():
    timmy.forward(10)


timmy = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="f",fun=forward_10)
screen.exitonclick()