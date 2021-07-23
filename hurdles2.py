from cs1robots import *
load_world("worlds/hurdles1.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.2)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        jump()

hubo.pick_beeper()