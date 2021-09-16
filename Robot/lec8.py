
from cs1robots import *
M = 0
X = 0
Y = 0
create_world()
edit_world()
hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.05)


def turn_right():
    for i in range(3):
        hubo.turn_left()


def moveSteps(steps):
    for i in range(steps):
        n = 0
        while hubo.on_beeper():
            n += 1
            hubo.pick_beeper()

        print n
        if n > M:
            p = hubo.get_pos()
            X = p[0]
            Y = p[1]
            m = n

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

print X, Y, M
