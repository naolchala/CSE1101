from cs1graphics import *

def create_hollow(rad, depth, outColor, inColor, move):
    x, y = move
    cout = Circle(rad)
    cout.setFillColor(inColor)
    cin = Circle(rad - depth)
    cin.setFillColor(outColor)
    cout.moveTo(x, y)
    cin.moveTo(x, y)
    return (cin, cout)

def create_tree(x, y, scale=1):
    tree = Layer()
    l = Rectangle(5, 20)
    l.move(0, 20)
    l.setFillColor("brown")
    tree.add(l)
    cir1 = Circle(10)
    cir2 = Circle(10)
    cir3 = Circle(10)
    cir1.setFillColor("green")
    cir1.setBorderWidth(0)
    cir2.setFillColor("green")
    cir2.setBorderWidth(0)
    cir2.move(5, 10)
    cir3.setFillColor("green")
    cir3.setBorderWidth(0)
    cir3.move(-5, 10)

    tree.add(cir1)
    tree.add(cir2)
    tree.add(cir3)
    tree.scale(scale)
    tree.moveTo(x, y)

    return tree


def create_light(x, y, scale=1):
    light = Layer()
    light.moveTo(x, y)
    light.scale(scale)
    
    pole = Polygon(
        Point(0, 0),
        Point(0, 100),
        Point(10, 100),
        Point(10, 10),
        Point(30, 10),
        Point(30, 0),
    )
    pole.setFillColor("white")

    bulb = Ellipse(20, 10)
    bulb.setBorderWidth(0)
    bulb.setFillColor("yellow")
    bulb.moveTo(20, 10)

    light.add(pole)
    light.add(bulb)
    return light