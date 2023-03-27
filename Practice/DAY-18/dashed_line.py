from turtle import  Turtle,Screen

timmy = Turtle()
# for _ in range(15):
#     timmy.down()
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)

for _ in range(15):
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    timmy.down()





screen = Screen()
screen.exitonclick()