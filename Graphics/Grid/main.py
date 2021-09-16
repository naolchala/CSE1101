from cs1graphics import *
from grid import *

world = Canvas(1000, 800)
grid = Grid(world, 10)

car = Layer()
body = Rectangle(50, 50)
body.setFillColor("green")
body.moveTo(25 + 100, 20 + 300)
car.add(body)

world.add(car)
