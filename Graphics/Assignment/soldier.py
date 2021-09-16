from cs1graphics import *
from weapon import *
from time import sleep
from math import sin


class Soldier:
    def __init__(self, world, color, face_color,  x=0, y=0):
        self.soldier = Layer()
        self.soldier.adjustReference(0, 100)
        self.world = world
        self.face_color = face_color
        self.color = color
        self.x = x
        self.y = y

        self.soldier.moveTo(x, y)
        self.create_solider()
        self.world.add(self.soldier)

    def create_solider(self):
        self.face = Layer()
        self.head = Circle(25)
        self.head.setFillColor(self.face_color)
        self.hair = Rectangle(50, 15)
        self.hair.setFillColor("black")
        self.hair.moveTo(0, -18)

        self.hair2 = Rectangle(10, 10)
        self.hair2.setFillColor("black")
        self.hair2.moveTo(-20, -5)

        self.leye = self.create_eye()
        self.leye.moveTo(0, 0)
        self.reye = self.create_eye()
        self.reye.moveTo(20, 0)

        self.mouth = Layer()
        self.mouth.moveTo(0, 13)
        self.mouth_white = Polygon(
            Point(0, -3), Point(15, 0), Point(13, 3), Point(0, 3))
        self.mouth_white.setFillColor("white")
        self.mouth.add(self.mouth_white)

        self.face.add(self.head)
        self.face.add(self.hair)
        self.face.add(self.hair2)
        self.face.add(self.leye)
        self.face.add(self.reye)
        self.face.add(self.mouth)

        self.middle = Layer()
        self.body = Polygon(
            Point(10, 0),
            Point(35, -10),
            Point(60, 0),
            Point(55, 50),
            Point(15, 50)
        )
        self.body.setFillColor(self.color)
        self.body.moveTo(-25, 20)

        self.left_hand = Layer()
        self.upper_left_hand = Polygon(
            Point(10, 0),
            Point(25, 0),
            Point(15, 15),
            Point(31, 35),
            Point(15, 35),
            Point(5, 15)
        )

        self.upper_left_hand.setFillColor(self.color)
        self.upper_left_hand.adjustReference(0, 0)

        self.lower_left_hand = Polygon(
            Point(15, 35),
            Point(31, 35),
            Point(37, 43),
            Point(35, 45),
            Point(30, 40),
            Point(25, 45),
            Point(13, 45),
        )
        self.lower_left_hand.setFillColor("black")

        self.left_hand.moveTo(-35, 25)
        self.left_hand.adjustReference(12.5, 3)
        self.left_hand.rotate(-60)

        self.left_hand.add(self.upper_left_hand)
        self.left_hand.add(self.lower_left_hand)
        self.left_hand.setDepth(-10)

        self.right_hand = Layer()
        self.upper_right_hand = Polygon(
            Point(10, 0),
            Point(25, 0),
            Point(20, 35),
            Point(5, 35)
        )

        self.upper_right_hand.setFillColor(self.color)
        self.upper_right_hand.adjustReference(0, 0)

        self.lower_right_hand = Polygon(
            Point(5, 35),
            Point(20, 35),
            Point(25, 42),
            Point(22, 45),
            Point(20, 41),
            Point(15, 47),
            Point(0, 45)
        )
        self.lower_right_hand.setFillColor("black")

        self.right_hand.moveTo(0, 25)
        self.right_hand.adjustReference(12.5, 3)
        self.right_hand.rotate(-20)
        self.right_hand.rotate(-60)

        self.right_hand.add(self.upper_right_hand)
        self.right_hand.add(self.lower_right_hand)

        self.middle.add(self.right_hand)
        self.middle.add(self.body)
        self.middle.add(self.left_hand)

        self.legs = Layer()
        self.left_leg = self.create_leg()
        self.left_leg.move(-10, 0)
        self.right_leg = self.create_leg()
        self.right_leg.move(10, 0)

        self.legs.add(self.left_leg)
        self.legs.add(self.right_leg)
        self.legs.moveTo(0, 75)

        self.soldier.add(self.legs)
        self.soldier.add(self.middle)
        self.soldier.add(self.face)

    def create_eye(self):
        eye_container = Layer()
        eye = Circle(4)
        eye.setFillColor("white")

        eye_ball = Circle(1)
        eye_ball.setFillColor("black")

        eye_brow = Polygon(Point(0, 0), Point(
            10, 0), Point(12, 4), Point(0, 2))
        eye_brow.moveTo(-5, -5)
        eye_brow.setFillColor("black")

        eye_container.add(eye)
        eye_container.add(eye_ball)
        eye_container.add(eye_brow)
        return eye_container

    def create_leg(self):
        leg = Layer()
        upper = Rectangle(20, 20)
        upper.setFillColor(self.color)

        sl = 20
        sh = 8

        shoe = Polygon(
            Point(0, 0),
            Point(0, sh),
            Point(sl, sh),
            Point(sl, 4),
            Point(15, 0)
        )

        shoe.move(-7.5, 10)
        shoe.setFillColor("brown")

        leg.add(upper)
        leg.add(shoe)
        return leg
