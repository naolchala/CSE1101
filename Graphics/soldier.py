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
        self.body = ClosedSpline(
            Point(10, 0),
            Point(30, -10),
            Point(60, 0),
            Point(60, 40),
            Point(35, 45),
            Point(0, 40)
        )
        self.body.setFillColor(self.color)
        self.body.moveTo(-25, 20)

        self.middle.add(self.body)

        self.legs = Layer()
        self.left_leg =  self.create_leg()
        self.left_leg.move(-13, 0)
        self.right_leg = self.create_leg()
        self.right_leg.move(13, 0)

        self.legs.add(self.left_leg)
        self.legs.add(self.right_leg)
        self.legs.moveTo(0, 75)

        self.soldier.add(self.legs)
        self.soldier.add(self.middle)
        self.soldier.add(self.face)

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

    def create_leg(self):
        leg = Layer()
        upper = Rectangle(15, 20)
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


solder1 = Soldier(world, "red", (210, 171, 156), 100, 100)