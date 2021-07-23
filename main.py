from cs1robots import *
create_world()
# creates a robot
hubo = Robot()

# drawing the path
hubo.set_trace("red")

# delaying the movement
hubo.set_pause(0.2)

# move
hubo.move()

# turn left
hubo.turn_left()