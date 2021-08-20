from cs1robots import *
load_world("C:\\Users\\astu\\Desktop\\intro\\Robot\\worlds\\harvest2.wld")

hubo = Robot(avenue=6, orientation="N")
hubo.set_pause(0.1)
hubo.set_trace("green")

def turn_right():
    for i in range(3):
        hubo.turn_left()

def up_step():
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()
    turn_right()
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()
    hubo.turn_left()

def down_step():
    

for i in range(5):
    up_step()
    
    
   
