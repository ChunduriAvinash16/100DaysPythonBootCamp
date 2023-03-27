from turtle import Turtle, Screen

my_timmy = Turtle()
for _ in range(4):
    my_timmy.forward(100)
    my_timmy.right(90)

screen = Screen()
screen.exitonclick()