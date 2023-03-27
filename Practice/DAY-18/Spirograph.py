import random
import turtle as t

t.colormode(255)

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


timmy = t.Turtle()
timmy.speed("fastest")
for _ in range(360 // 5):
    timmy.pencolor(generate_color())
    timmy.circle(100)
    timmy.left(5)

t.Screen().exitonclick()
