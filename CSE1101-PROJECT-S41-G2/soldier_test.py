from cs1graphics import *
from soldier import *
from weapon import *
from configuration import *
from time import sleep

canvas = Canvas(700, 600)
s1 = Soldier(canvas, "darkgreen", ita_skin[1], 100, 300)
ak1 = Ak(canvas, 100, 225)

for i in range(50):
    s1.left_hand.move(sin(i) * 5, 0)
    s1.right_hand.move(sin(i) * 5, 0)
    ak1.weapon.move(sin(i) * 5, 0)
    bullet = Ellipse(5, 2)
    bullet.moveTo(150, 225)
    bullet.setFillColor("orange")
    canvas.add(bullet)

    for i in range(50):
        bullet.move(10, 0)

    canvas.remove(bullet)
