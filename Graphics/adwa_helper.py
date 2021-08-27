from cs1graphics import *
def create_sun(color, radius):
    sun = Circle(radius)
    sun.setFillColor(color)
    sun.setBorderWidth(0)
    sun.moveTo(800, 400)
    return sun
