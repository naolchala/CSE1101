from cs1robots import *
create_world()

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

hubo = Robot()
hubo.set_pause(0.2)
hubo.set_trace("red")

for i in range(14):
    if i > 0 and i % 4 == 0:
        turn_right(hubo)
    elif i > 0 and i % 2 == 0:
        hubo.turn_left()

    hubo.move()