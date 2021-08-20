from cs1robots import *
load_world("C:\\Users\\astu\\Desktop\\intro\\Robot\\worlds\\trash1.wld")

hubo = Robot(color="green")
hubo.set_pause(0.1)

def turn_around():
    for i in range(2):
        hubo.turn_left()

def turn_right():
    for i in range(3):
        hubo.turn_left()
    
def go_and_pick():
    while hubo.front_is_clear():
        while hubo.on_beeper():
            hubo.pick_beeper()

        hubo.move()

def drop_all_beeper():
    while hubo.carries_beepers():
        hubo.drop_beeper()

go_and_pick()
turn_around()
go_and_pick()
turn_right()
hubo.move()
drop_all_beeper()
turn_around()
hubo.move()

