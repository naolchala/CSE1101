from cs1graphics import *
from soldier import *
from weapon import *
from configuration import *
from time import sleep

canvas = Canvas(700, 600)
s1 = Soldier(canvas, "darkgreen", ita_skin[1], 100, 300)
# s1.left_hand.rotate(-200)
# w1 = Arrow(canvas, 20, 180)
# w1.arrow.rotate(-45)

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
# for i in range(45):
#     s1.left_hand.rotate(-1)
#     w1.arrow.move(-1, 1)
#     sleep(.02)

# for i in range(20):
#     s1.left_hand.rotate(3)
#     w1.arrow.move(1, -1)
#     sleep(.01)

# w1.arrow.adjustReference(0, 0)
# for i in range(45):
#     w1.arrow.move(6.667, -3)
#     w1.arrow.rotate(1)
#     sleep(.01)

# for i in range(45):
#     w1.arrow.move(6.667, 3)
#     w1.arrow.rotate(1)
#     sleep(.01)
