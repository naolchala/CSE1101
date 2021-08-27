from cs1graphics import *
canvas = Canvas(300, 300)
body = ClosedSpline(Point(50, 100), Point(100, 80), Point(150, 100), Point(160, 200), Point(100, 220), Point(40, 200))
body.setFillColor("darkgreen")
canvas.add(body)