from cs1robots import *
load_world("/home/cisco/Desktop/Programming/Python/CSE1101/Robot/worlds/rain1.wld")
hubo = Robot(orientation='N')
hubo.set_trace("blue")
hubo.set_pause(0.15)


def turn_right():
    for i in range(3):
        hubo.turn_left()
