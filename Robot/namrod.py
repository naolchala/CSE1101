from cs1robots import *
size = int(raw_input("size: "))
width = size + 2
create_world(size+2, size+2)


def turn_right():
    for i in range(3):
        hubo.turn_left()


hubo = Robot(beepers=50)
hubo.set_pause(0.1)
center = (width/2) + 1

for i in range(center - 1):
    hubo.move()


hubo.turn_left()

while not hubo.on_beeper():
    if hubo.right_is_clear():
        hubo.move()
        hubo.drop_beeper()
        turn_right()
        hubo.move()
        hubo.turn_left()
    elif hubo.front_is_clear():
        hubo.move()
        hubo.drop_beeper()
        hubo.turn_left()
