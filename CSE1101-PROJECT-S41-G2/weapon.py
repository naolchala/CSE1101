from cs1graphics import *
from configuration import *
from math import sin
from time import sleep


class Ak:
    def __init__(self, world, x=0, y=0):
        self.weapon = Layer()
        world.add(self.weapon)
        self.weapon.moveTo(x, y)
        w = Polygon(
            Point(5, 3),
            Point(0, 20),
            Point(20, 15),
            Point(20, 18),
            Point(24, 15),
            Point(24, 13),
            Point(30, 10),
            Point(35, 10),
            Point(35, 13),
            Point(45, 13),
            Point(45, 10),
            Point(50, 10),
            Point(50, 20),
            Point(65, 20),
            Point(65, 10),
            Point(100, 3),
            Point(100, 0),
            Point(40, 0),
            Point(40, 3),
            Point(30, 3),
            Point(27, 0)
        )
        w.setFillColor(akwod)
        self.weapon.add(w)


class Arrow:
    def __init__(self, world, x=0, y=0):
        self.weapon = Layer()
        self.weapon.moveTo(x, y)
        world.add(self.weapon)
        stick = Path(
            Point(0, 0),
            Point(100, 0)
        )
        stick.setBorderWidth(2)
        stick.setArrows(True)
        stick.setBorderColor("darkgray")
        self.weapon.adjustReference(50, 0)
        self.weapon.add(stick)


class Shield:
    def __init__(self, world, x, y):
        self.shield = Layer()
        self.shield.moveTo(x, y)
        self.body = Ellipse(50, 70)
        self.body.setFillColor("brown")
        self.body.setBorderWidth(5)
        self.shield.add(self.body)
        world.add(self.shield)
