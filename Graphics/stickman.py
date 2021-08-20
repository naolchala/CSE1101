from cs1graphics import *
import time

world = Canvas(1000, 600)
THICKNESS = 4
class Stickman:
    def __init__(self, world):
        self.man = Layer()
        self.man.moveTo(100, 100)
        self.create_person()
        world.add(self.man)
        
    def create_person(self):
        self.upper_body = Layer()
        self.head = Circle(30)
        self.head.setBorderColor("black")
        self.head.setBorderWidth(THICKNESS)

        self.neck = Path(Point(0, 30), Point(0, 30+35))
        self.neck.setBorderWidth(THICKNESS)
        
        self.upper_body.add(self.head)
        self.upper_body.add(self.neck)

        self.center_body  = Layer()
        self.body_line =  Path(Point(0, 30+35), Point(0, 30+35+100))
        self.body_line.setBorderWidth(THICKNESS)

        self.right_hand = Layer()
        self.right_arm = Path(Point(0, 30+35), Point(-45, 30+35+50))
        self.right_hand.add(self.right_arm)
        self.right_arm.setBorderWidth(THICKNESS)
        self.left_hand = Layer()

        
        self.center_body.add(self.body_line)
        self.center_body.add(self.right_hand)
        self.center_body.add(self.left_hand)


        self.man.add(self.upper_body)
        self.man.add(self.center_body)

man = Stickman(world)

# for i in range(45):
#     man.upper_body.rotate(1)
#     time.sleep(0.1)
    
    