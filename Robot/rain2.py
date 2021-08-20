from cs1robots import *
load_world("worlds/rain1.wld")
hubo = Robot(orientation='N')
hubo.set_trace("blue")
hubo.set_pause(0.15)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def moveStep(step):
    for i in range(step):
        hubo.move()

moveStep(5)
turn_right()
moveStep(2)
turn_right()
moveStep(2)
hubo.turn_left()
moveStep(5)
hubo.turn_left()
moveStep(4)
hubo.turn_left()
moveStep(5)
hubo.turn_left()
moveStep(2)
turn_right()
moveStep(2)
hubo.turn_left()
moveStep(5)