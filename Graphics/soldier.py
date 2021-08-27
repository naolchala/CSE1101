from cs1graphics import *

world=Canvas(500, 500)

class Soldier:
    def __init__(self, world, color, face_color,  x=0, y=0):
        self.soldier = Layer()
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
        self.leye.moveTo(0,0)
        self.reye = self.create_eye()
        self.reye.moveTo(20, 0)

        self.mouth = Layer()
        self.mouth.moveTo(0, 13)
        self.mouth_white = Polygon(Point(0,-3), Point(15, 0), Point(13, 3), Point(0, 3)) 
        self.mouth_white.setFillColor("white")
        self.mouth.add(self.mouth_white)

        self.face.add(self.head)
        self.face.add(self.hair)
        self.face.add(self.hair2)
        self.face.add(self.leye)
        self.face.add(self.reye)
        self.face.add(self.mouth)

        self.middle  = Layer()
        self.body = ClosedSpline(Point(0, 20), Point(40, 0), Point(60, 20), Point(70, 50), Point(40, 60), Point(10, 50))
        self.body.setFillColor(self.face_color)

        self.middle.add(self.body)
        self.legs = Layer()

        self.soldier.add(self.face)
        self.soldier.add(self.middle)
        self.soldier.add(self.legs)

    def create_eye(self):
        eye_container=Layer()
        eye = Circle(4)
        eye.setFillColor("white")

        eye_ball = Circle(1)
        eye_ball.setFillColor("black")

        eye_brow = Polygon(Point(0, 0), Point(10, 0), Point(12, 4), Point(0, 2))
        eye_brow.moveTo(-5, -5)
        eye_brow.setFillColor("black")


        eye_container.add(eye)
        eye_container.add(eye_ball)
        eye_container.add(eye_brow)
        return eye_container

solder1 = Soldier(world, "red", (210, 171, 156), 100, 100)