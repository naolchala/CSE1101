from cs1graphics import *
WIDTH = 680
HEIGHT = 460

world = Canvas(WIDTH, HEIGHT, title="Car Animation")

class Car:
    def __init__(self, world, x, y):
        self.x = x
        self.y = y
        self.car = Layer()
        self.car.moveTo(self.x, self.y)
        self.world = world
        self.create_body()

        self.world.add(self.car)

    def create_body(self):
        self.create_upper_body()
        self.create_center_body()

    def create_upper_body(self):
        self.upper_body = Layer()
        back_triangle = Polygon(Point(0, 100), Point(100,100), Point(100, 0), Point(0,100))
        back_triangle.setBorderColor("red")
        back_triangle.setFillColor("red")

        center_rectangle = Rectangle(160, 100)
        center_rectangle.setFillColor("red")
        center_rectangle.setBorderColor("red")
        center_rectangle.moveTo(100 + 80, 0 + 50)

        front_triangle = Polygon(Point(0, 0), Point(0,100), Point(100, 100), Point(0,0))
        front_triangle.setBorderColor("red")
        front_triangle.setFillColor("red")
        front_triangle.moveTo(100 + 160, 0)

        self.upper_body.add(center_rectangle)
        self.upper_body.add(back_triangle)
        self.upper_body.add(front_triangle)
        self.car.add(self.upper_body)

    def create_center_body(self):
        self.center_body = Layer()
        center_width = 100 + 160 + 100 + 100
        center  = Rectangle(center_width, 150)
        center.setFillColor("red")
        center.setBorderColor("red")
        center.moveTo(center_width/2, 100 + 75)

        self.center_body.add(center)
        self.car.add(self.center_body)


class Tire()

Car(world, 10, 20)
