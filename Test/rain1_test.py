from cs1robots import *
load_world("/home/cisco/Desktop/Programming/Python/CSE1101/Robot/worlds/rain1.wld")
hubo = Robot(avenue=3, street=6, beepers=10)
hubo.turn_left()
hubo.set_trace("blue")
hubo.set_pause(0.05)


def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo.move()
while hubo.get_pos() != (3, 6):
    if hubo.front_is_clear():
        if hubo.left_is_clear():
            hubo.drop_beeper()

        hubo.move()
    else:
        turn_right()

hubo.turn_left()
hubo.move()
for i in range(2):
    hubo.turn_left()
