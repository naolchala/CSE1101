from cs1robots import *
load_world("/home/cisco/Desktop/Programming/Python/CSE1101/Robot/worlds/trash4.wld")

hubo = Robot(color="green")
hubo.set_pause(0.01)
hubo.set_trace("blue")


def turn_around():
    for i in range(2):
        hubo.turn_left()


def turn_right():
    for i in range(3):
        hubo.turn_left()


def pick_all():
    while hubo.on_beeper():
        hubo.pick_beeper()


pick_all()
while hubo.get_pos() != (10, 11):
    if hubo.front_is_clear():
        hubo.move()
        pick_all()
    else:
        hubo.turn_left()
        if hubo.facing_north():
            hubo.move()
            hubo.turn_left()
            pick_all()
        else:
            turn_around()
            hubo.move()
            turn_right()
            pick_all()
