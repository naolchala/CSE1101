from cs1graphics import *
from adwa_helper import create_sun
from soldier import *
from configuration import *
from weapon import *
from random import randint

world = Canvas(WIDHT, HEIGHT, bgColor=background)

# background
ground = Rectangle(1600, 300)
ground.setFillColor(ground_color)
ground.setBorderWidth(0)
ground.moveTo(800, 600 + 150)

mountains = Polygon(Point(0, 400), Point(100, 350), Point(250, 450), Point(400, 300), Point(500, 400), Point(600, 250), Point(750, 480), Point(850, 300), Point(
    1000, 450), Point(1100, 200), Point(1150, 250), Point(1200, 150), Point(1400, 400), Point(1500, 250), Point(1600, 450), Point(1600, 600), Point(0, 600))
mountains.setFillColor(mountains_color)
mountains.setBorderWidth(0)


mountains_back = Polygon(Point(80, 400), Point(180, 350), Point(250 + 80, 450), Point(480, 300), Point(580, 400), Point(680, 250), Point(750+80, 480), Point(850+80, 300), Point(
    1080, 450), Point(1180, 200), Point(1150 + 80, 250), Point(1200 + 80, 150), Point(1400 + 80, 400), Point(1500 + 80, 250), Point(1600 + 80, 450), Point(1600, 600), Point(0, 600))
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


# soldiers
eths = []
etw = []
for i in range(3):
    skin = randint(0, len(eth_skin) - 1)
    et = Soldier(world, "white", eth_skin[skin], -100, ground_pos)
    et.left_hand.rotate(-120)
    eths.append(et)

itas = []

for i in range(3):
    skin = randint(0, len(ita_skin) - 1)
    it = Soldier(world, "darkgreen", ita_skin[skin], WIDHT+100, ground_pos)
    it.soldier.flip(180)
    itas.append(it)

for i in range(3):
    for j in range((150 + 100*i)/5):
        eths[i].left_leg.move(0, sin(j)*2)
        eths[i].right_leg.move(0, sin(j)*-2)
        eths[i].soldier.move(5, 0)
        sleep(.02)

    for j in range((150 + 100*i)/5):
        itas[i].left_leg.move(0, sin(j)*2)
        itas[i].right_leg.move(0, sin(j)*-2)
        itas[i].soldier.move(-5, 0)
        sleep(.02)
