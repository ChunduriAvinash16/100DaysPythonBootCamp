
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def front_is_clear():
    pass
def right_is_clear():
    pass
def move():
    pass
    #move forward
def turn_left():
    pass
    #turn_left
def at_goal():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
