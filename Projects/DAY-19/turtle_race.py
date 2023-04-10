from turtle import Turtle,Screen
from random import randint

is_raceOn = False
screen = Screen()

#Setting up the Screen width and height
screen.setup(width=500,height=400)

#User input
user_bet= screen.textinput(title="Make your bet",prompt="Which turtle win the race? Enter a color: ")
colors = ["red","orange","yellow","green","purple","blue"]
y_cordinates = [100,60,20,-20,-60,-100]
all_turtles = []
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_cordinates[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_raceOn = True

while is_raceOn:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_raceOn = False
            winnig_color = turtle.pencolor()
            if winnig_color == user_bet:
                print(f"you've won! the {winnig_color} turtle is the winner!")
            else:
                print(f"you've lose! the {winnig_color} turtle is the winner!")
        moving_distance = randint(0,10)
        turtle.forward(moving_distance)

screen.exitonclick()