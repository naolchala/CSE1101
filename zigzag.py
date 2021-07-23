from cs1robots import *
create_world()

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def moveSteps(steps):
    for i in range(steps):
        hubo.move()

def goUpAndComeDown():
    hubo.turn_left()
    moveSteps(9)
    turn_right()
    hubo.move()
    turn_right()
    moveSteps(9)
    hubo.turn_left()

for i in range(5):
    if i > 0:
        hubo.move()
    
    goUpAndComeDown()

