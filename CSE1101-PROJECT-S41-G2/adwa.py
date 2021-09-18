from cs1graphics import *
from grid import *
from adwa_helper import *
from soldier import *
from configuration import *
from weapon import *
from random import randint

world = Canvas(WIDHT, HEIGHT, bgColor=background)
# g = Grid(world, 20)

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

# Ethiopians
eths = []
eth_weapons = []
eth_shilds = []
for i in range(3):
    skin = randint(0, len(eth_skin) - 1)
    et = Soldier(world, "white", eth_skin[skin], -100, ground_pos)
    et.left_hand.rotate(-120)
    eths.append(et)

    weap = Arrow(world, -150, ground_pos-110)
    sh = Shield(world, -40, ground_pos-70)
    eth_weapons.append(weap)
    eth_shilds.append(sh)


# ITALINAS
itas = []
ita_weapons = []
for i in range(3):
    skin = randint(0, len(ita_skin) - 1)
    it = Soldier(world, "darkgreen", ita_skin[skin], WIDHT+100, ground_pos)
    it.soldier.flip(180)
    itas.append(it)

    iw = Ak(world, WIDHT+100, ground_pos-80)
    iw.weapon.flip(180)
    ita_weapons.append(iw)


# Entrance Movement
for i in range(len(eths)):
    for j in range((150 + 100*i)/5):
        eths[i].left_leg.move(0, sin(j)*2)
        eths[i].right_leg.move(0, sin(j)*-2)
        soldier_move(eths[i], eth_weapons[i], 5, 0, eth_shilds[i])
        sleep(.02)

    for j in range((150 + 100*i)/5):
        itas[i].left_leg.move(0, sin(j)*2)
        itas[i].right_leg.move(0, sin(j)*-2)
        soldier_move(itas[i], ita_weapons[i], -5, 0)
        sleep(.02)

title = Text("ADWA", 80)
title.setFontColor(sun_color)
title.moveTo(740, 140)
world.add(title)

sleep(.2)

textcolor = list(sun_color)
for i in range(70):
    for j in range(len(textcolor)):
        textcolor[j] -= 1
    title.setFontColor(tuple(textcolor))
    sleep(.005)

sleep(.6)

for i in range(70):
    for j in range(len(textcolor)):
        textcolor[j] += 1
    title.setFontColor(tuple(textcolor))
    sleep(.005)

world.remove(title)

for i in range(len(eth_weapons)):
    eth_weapons[i].weapon.adjustReference(0, 0)
    ipos = ita_weapons[i].weapon.getReferencePoint().getX()
    epos = eth_weapons[i].weapon.getReferencePoint().getX()
    scale = (ipos - epos)/(45*2)

    for j in range(45):
        eths[i].left_hand.rotate(-1)
        eth_weapons[i].weapon.rotate(-1)
        eth_weapons[i].weapon.move(-1, 0)

    sleep(.05)
    for j in range(20):
        eths[i].left_hand.rotate(3)
        eth_weapons[i].weapon.move(1, 0)
        sleep(.01)

    for j in range(45):
        eth_weapons[i].weapon.move(scale, -6)
        eth_weapons[i].weapon.rotate(1)
        sleep(.01)

    for j in range(45):
        eth_weapons[i].weapon.move(scale, 6)
        eth_weapons[i].weapon.rotate(1)
        sleep(.01)

    for j in range(90):
        itas[i].soldier.rotate(1)
        eth_weapons[i].weapon.move(1, 1)
        ita_weapons[i].weapon.move(1, 1)
        sleep(.0005)

sleep(1)

for i in range(len(itas)):
    world.remove(itas[i].soldier)
    world.remove(ita_weapons[i].weapon)
    world.remove(eth_weapons[i].weapon)


itas = []
ita_weapons = []
for i in range(3):
    skin = randint(0, len(ita_skin) - 1)
    it = Soldier(world, "darkgreen", ita_skin[skin], WIDHT+100, ground_pos)
    it.soldier.flip(180)
    itas.append(it)

    iw = Ak(world, WIDHT+100, ground_pos-80)
    iw.weapon.flip(180)
    ita_weapons.append(iw)

for i in range(len(itas)):
    for j in range((150 + 100*i)/5):
        itas[i].left_leg.move(0, sin(j)*2)
        itas[i].right_leg.move(0, sin(j)*-2)
        soldier_move(itas[i], ita_weapons[i], -5, 0)
        sleep(.02)

for i in range(3):
    for j in range(len(itas)):
        itas[j].left_hand.move(sin(i) * 5, 0)
        itas[j].right_hand.move(sin(i) * 5, 0)
        ita_weapons[j].weapon.move(sin(i) * 5, 0)
        bullet = Ellipse(10, 5)
        bu_pos = ita_weapons[j].weapon.getReferencePoint().get()
        bullet.moveTo(bu_pos[0], bu_pos[1])
        bullet.setFillColor("red")
        world.add(bullet)

        for k in range(500):
            bullet.move(-10, 0)

        world.remove(bullet)

    deg = 90
    s = 1
    for k in range(deg/s):
        eths[2-i].soldier.rotate(-1)
        eth_shilds[2-i].shield.move(-1, 1)
        eth_shilds[2-i].shield.rotate(-1)

sleep(1)
for i in range(len(eths)):
    world.remove(eths[i].soldier)
    world.remove(eth_shilds[i].shield)


eths = []
eth_weapons = []
eth_shilds = []
for i in range(3):
    skin = randint(0, len(eth_skin) - 1)
    et = Soldier(world, "white", eth_skin[skin], -100, ground_pos)
    et.left_hand.rotate(-120)
    eths.append(et)

    weap = Arrow(world, -150, ground_pos-110)
    sh = Shield(world, -40, ground_pos-70)
    eth_weapons.append(weap)
    eth_shilds.append(sh)

for i in range(len(eths)):
    for j in range((150 + 100*i)/5):
        eths[i].left_leg.move(0, sin(j)*2)
        eths[i].right_leg.move(0, sin(j)*-2)
        soldier_move(eths[i], eth_weapons[i], 5, 0, eth_shilds[i])
        sleep(.02)


for i in range(len(eth_weapons)):
    eth_weapons[i].weapon.adjustReference(0, 0)
    ipos = ita_weapons[i].weapon.getReferencePoint().getX()
    epos = eth_weapons[i].weapon.getReferencePoint().getX()
    scale = (ipos - epos)/(45*2)

    for j in range(45):
        eths[i].left_hand.rotate(-1)
        eth_weapons[i].weapon.rotate(-1)
        eth_weapons[i].weapon.move(-1, 0)

    sleep(.05)
    for j in range(20):
        eths[i].left_hand.rotate(3)
        eth_weapons[i].weapon.move(1, 0)
        sleep(.01)

    for j in range(45):
        eth_weapons[i].weapon.move(scale, -6)
        eth_weapons[i].weapon.rotate(1)
        sleep(.01)

    for j in range(45):
        eth_weapons[i].weapon.move(scale, 6)
        eth_weapons[i].weapon.rotate(1)
        sleep(.01)

    for j in range(90):
        itas[i].soldier.rotate(1)
        eth_weapons[i].weapon.move(1, 1)
        ita_weapons[i].weapon.move(1, 1)
        sleep(.0005)

sleep(1)

for j in range((150 + 100*i)/5):
    for i in range(len(eths)):
        eths[i].left_leg.move(0, sin(j)*2)
        eths[i].right_leg.move(0, sin(j)*-2)
        soldier_move(eths[i], None, 5, 0, eth_shilds[i])
        sleep(.02)

for i in range(20):
    for j in range(len(eths)):
        eths[j].right_hand.move(0, sin(i) * 4)
        eths[j].left_hand.move(0, sin(i) * 4)
        eth_shilds[j].shield.move(0, sin(i) * 4)
# Name
students = [
    {
        "name": "Naol Chala",
        "id": "UGR/22527/13"
    },
    {
        "name": "Amanuel Bedlu",
        "id": "UGR/22637/13"
    },
    {
        "name": "Firaol Taha",
        "id": "UGR/22925/13"
    },
    {
        "name": "Esrom Seifu",
        "id": "UGR/23668/13"
    },
    {
        "name": "Abraham Atlabachew",
        "id": "UGR/23606/13"
    }
]


T = Text("Made In Section 41", 35)
T.setFontColor(mountains_color)
world.add(T)
T.move(740, 100)

for i in students:
    t = Text(i['name'], 30)
    i = Text(i['id'], 20)
    t.setFontColor(sun_color)
    i.setFontColor(sun_color)
    t.moveTo(740, 180)
    i.moveTo(740, 210)

    world.add(i)
    world.add(t)
    textcolor = list(sun_color)
    fade_in(t, textcolor)
    fade_in(i)
    sleep(2)
    world.remove(t)
    world.remove(i)
