#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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
def step_left():
    move()
    turn_left()
def step_right():
    move()
    turn_right()
def jump():
    step_left()
    step_right()
    step_right()
    step_left()
while not at_goal():
    jump()