from cs1graphics import *
from adwa_helper import create_sun

background = (238, 167, 87)
ground_color = (34, 20, 37)
mountains_color = (217, 99, 38)
mountains_back_color = (232, 164, 89)
sun_color = (241, 244, 180)
sun_color2 = (234, 207, 131)
sun_color3 = (235, 194, 114) 

world = Canvas(1600, 800, bgColor=background)
ground = Rectangle(1600, 300)
ground.setFillColor(ground_color)
ground.setBorderWidth(0)
ground.moveTo(800, 600 + 150)

mountains = Polygon(Point(0, 400), Point(100, 350), Point(250, 450), Point(400, 300), Point(500, 400), Point(600, 250), Point(750, 480), Point(850, 300), Point(1000, 450), Point(1100, 200), Point(1150, 250), Point(1200, 150), Point(1400, 400), Point(1500, 250), Point(1600, 450), Point(1600, 600), Point(0, 600))
mountains.setFillColor(mountains_color)
mountains.setBorderWidth(0)


mountains_back = Polygon(Point(80, 400), Point(180, 350), Point(250 + 80, 450), Point(480, 300), Point(580, 400), Point(680, 250), Point(750+80, 480), Point(850+80, 300), Point(1080, 450), Point(1180, 200), Point(1150 + 80, 250), Point(1200 + 80, 150), Point(1400 + 80 , 400), Point(1500 + 80, 250), Point(1600 + 80, 450), Point(1600, 600), Point(0, 600))
mountains_back.setFillColor(mountains_back_color)
mountains_back.setBorderWidth(0)

sun1 = create_sun(sun_color, 500)
sun2 = create_sun(sun_color2, 550)
sun3 = create_sun(sun_color3, 600)

world.add(sun3)
world.add(sun2)
world.add(sun1)
world.add(ground)
world.add(mountains_back)
world.add(mountains)