import random

import colorgram
import turtle as t

t.colormode(255)


def generate_color_from_image(no_of_colors):
    colors = colorgram.extract("image.jpg", no_of_colors)
    colors_list = []
    for i in range(no_of_colors):
        colors_list.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
    return colors_list


color_list = generate_color_from_image(15)
timmy = t.Turtle()
timmy.hideturtle()
timmy.up()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")

# for i in range(10):
#     for _ in range(9):
#         timmy.dot(20, random.choice(color_list))
#         timmy.forward(50)
#     timmy.dot(20, random.choice(color_list))
#     if i % 2 == 0:
#         timmy.left(90)
#         timmy.forward(50)
#         timmy.left(90)
#     else:
#         timmy.right(90)
#         timmy.forward(50)
#         timmy.right(90)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


t.Screen().exitonclick()
