from cs1graphics import *
import time

world = Canvas(1000, 600)
THICKNESS = 10

class Stickman:
    def __init__(self, world, x, y):
        self.man = Layer()
        self.man.moveTo(x, y)
        self.create_person()
        world.add(self.man)
        
    def create_person(self):
        self.upper_body = Layer()
        self.upper_body.adjustReference(0, 30+35)

        self.head = Circle(30)
        self.head.setBorderColor("black")
        self.head.setBorderWidth(THICKNESS)

        self.neck = Path(Point(0, 30), Point(0, 30+35))
        self.neck.setBorderWidth(THICKNESS)
        
        self.upper_body.add(self.head)
        self.upper_body.add(self.neck)

        self.center_body = Layer()
        self.body_line = Path(self.neck.getPoint(1), Point(0, 30+35+100))
        self.body_line.setBorderWidth(THICKNESS)

        self.right_hand = Layer()
        self.right_hand.adjustReference(0, 30+35)

        self.right_arm = Path(Point(0, 30+35), Point(-45, 30+35+50))
        self.right_arm.setBorderWidth(THICKNESS)

        self.right_wrist = Path(self.right_arm.getPoints()[1], Point(-45-20, 30+35+50+50))
        self.right_wrist.setBorderWidth(THICKNESS)

        self.right_hand.add(self.right_arm)
        self.right_hand.add(self.right_wrist)

        self.left_hand = Layer()
        self.left_hand.adjustReference(0, 30+35)
        self.left_arm = Path(Point(0, 30+35), Point(45, 30+35+50))
        self.left_arm.setBorderWidth(THICKNESS)
        
        self.left_wrist = Path(self.left_arm.getPoints()[1], Point(45+20, 30+35+50+45))
        self.left_wrist.setBorderWidth(THICKNESS)

        self.left_hand.add(self.left_arm)
        self.left_hand.add(self.left_wrist)
        
        self.center_body.add(self.body_line)
        self.center_body.add(self.right_hand)
        self.center_body.add(self.left_hand)

        self.lower_body = Layer()
        

        self.right_leg = Layer()
        self.right_leg.adjustReference(self.body_line.getPoint(1).get()[0], self.body_line.getPoint(1).get()[1])
        self.right_upper_leg = Path(self.body_line.getPoints()[1], Point(-35, 30+35+100+100))
        self.right_upper_leg.setBorderWidth(THICKNESS)
        self.right_lower_leg = Path(self.right_upper_leg.getPoints()[1], Point(-35-15, 30+35+100+100+ 100))
        self.right_lower_leg.setBorderWidth(THICKNESS)
        self.right_leg.add(self.right_upper_leg)
        self.right_leg.add(self.right_lower_leg)
        
        self.left_leg = Layer()
        self.left_leg.adjustReference(self.body_line.getPoint(1).get()[0], self.body_line.getPoint(1).get()[1])
        self.right_upper_leg = Path(self.body_line.getPoints()[1], Point(-35, 30+35+100+100))
        self.left_upper_leg = Path(self.body_line.getPoints()[1], Point(35, 30+35+100+100))
        self.left_upper_leg.setBorderWidth(THICKNESS)
        self.left_lower_leg = Path(self.left_upper_leg.getPoints()[1], Point(35+15, 30+35+100+100+ 100))
        self.left_lower_leg.setBorderWidth(THICKNESS)
        self.left_leg.add(self.left_upper_leg)
        self.left_leg.add(self.left_lower_leg)

        self.lower_body.add(self.right_leg)
        self.lower_body.add(self.left_leg)


        self.man.add(self.upper_body)
        self.man.add(self.center_body)
        self.man.add(self.lower_body)

    def move(self, pixels):
        for i in range(pixels):
            self.man.move(1, 0)

    def say_hi(self):
        for i in range(65):
            self.right_hand.rotate(1)
            self.left_hand.rotate(5)
            if i < 45:
                self.right_wrist.rotate(2)
            time.sleep(0.01)
        while True:
            for i in range(35):
                self.right_hand.rotate(-1)
                time.sleep(0.01)
                
            for i in range(35):
                self.right_hand.rotate(1)
                time.sleep(0.01)

    def walk(self):
        self.left_wrist.rotate(-45)


        for i in range(45):
            self.right_hand.rotate(-2)
            self.left_hand.rotate(2)
            
            self.left_leg.rotate(1)
            self.right_leg.rotate(-1)

            self.right_lower_leg.rotate(0.5)
            self.left_lower_leg.rotate(-0.5)
            time.sleep(0.01)
        
        
        for i in range(45):
            self.right_hand.rotate(2)
            self.left_hand.rotate(-2)
            self.left_leg.rotate(-1)
            self.right_leg.rotate(1)

            self.right_lower_leg.rotate(-0.5)
            self.left_lower_leg.rotate(0.5)
            time.sleep(0.01)
        
        self.left_wrist.rotate(45)
        

    def go(self, pixels):
        for i in range(pixels):
            self.man.move(20, 0)
            self.walk()


def move(object, pixels, xfactor=0, yfactor=0):
    for i in range(pixels):
        object.move(xfactor, yfactor)

def rotate(drawable, degree, factor=1):
    for i in range(degree):
        drawable.rotate(factor)

man = Stickman(world, 100, 100)
man.go(400)