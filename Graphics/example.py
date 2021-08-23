from cs1graphics import *

world  = Canvas(1000, 1000, bgColor=(00, 60, 60))

rects = []
for i in range(25):
    r = Rectangle((i+1)*(i+1), (i+1)*(i+1))
    r.setBorderColor("yellow")
    r.setBorderWidth(5)
    r.moveTo(500, 500)
    world.add(r)

    rects.append(r)

while True:
    for i in range(len(rects)):
        f = 2 if i % 3 == 0 else 1
        if i % 2 == 0:
            rects[i].rotate(i)
        else:
            rects[i].rotate(-1*i)