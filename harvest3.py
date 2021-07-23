from cs1robots import *
load_world("worlds/harvest3.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def moveSteps(step):
    for i in range(step):
        hubo.move()
        if hubo.on_beeper():
            hubo.pick_beeper()
        

moveSteps(6)
hubo.turn_left()
moveSteps(1)
hubo.turn_left()
moveSteps(5)