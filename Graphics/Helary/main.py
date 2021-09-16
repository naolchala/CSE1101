from cs1graphics import *
from helper import *
from Config import *

world = Canvas(WIDTH, HEIGHT)

# Gate
Gada = Layer()
Gada.moveTo(400, HEIGHT/2 + 200)

c1 = Circle(200)
c1.setBorderWidth(THICKNESS)
c1.setBorderColor(circle_color)

c2 = Circle(300)
c2.setBorderWidth(THICKNESS)
c2.setBorderColor(circle_color)
c2.moveTo(270, 0)

c3 = Circle(400)
c3.setBorderWidth(THICKNESS)
c3.setBorderColor(circle_color)
c3.moveTo(500, 0)


c4 = Circle(250)
c4.setBorderWidth(THICKNESS)
c4.setBorderColor(circle_color)
c4.moveTo(830, 0)


c5 = Circle(160)
c5.setBorderWidth(THICKNESS-5)
c5.setBorderColor(circle_color)
c5.moveTo(740, 0)

lines = [
    [(550, -110), (730, -320)],
    [(530, -150), (650, -380)],
    [(490, -200), (580, -400)],
    [(460, -240), (500, -400)],
    [(410, -260), (420, -400)],
    [(370, -290), (350, -360)],
    [(320, -300), (290, -340)]
]

for line in lines:
    sx, sy = line[0]
    ex, ey = line[1]

    l1 = Path(Point(sx, sy), Point(ex, ey))
    l1.setBorderWidth(THICKNESS-10)
    l1.setBorderColor("orange")
    Gada.add(l1)


left_gate_wall = ClosedSpline(
    Point(-200, 0),
    Point(-200, -50),
    Point(-150, -150),
    Point(-100, -170),
    Point(-50, -200),
    Point(0, -210),
    Point(40, -190),
    Point(20, -160),
    Point(0, -100),
    Point(-30, -10),
    Point(-30, 0),
    Point(-60, 0),
    Point(-150, 0),
    Point(-200, 0)

)

left_gate_wall.setFillColor("orange")
left_gate_wall.setBorderWidth(0)
Gada.add(left_gate_wall)

right_gate_wall = Polygon(
    Point(900, 0),
    Point(1080, 0),
    Point(1080, -50),
    Point(1020, -150),
    Point(980, -190),
    Point(920, -230),
    Point(880, -250),
    Point(830, -250),
    Point(880, -150)
)
right_gate_wall.setFillColor("orange")
right_gate_wall.setBorderWidth(0)
Gada.add(right_gate_wall)

Gada.add(c1)
Gada.add(c2)
Gada.add(c3)
Gada.add(c4)
Gada.add(c5)

cover = Rectangle(WIDTH+40, HEIGHT/2)
cover.setBorderWidth(0)
cover.setFillColor(asphalt_color)
cover.moveTo(WIDTH/2-220, 180)
Gada.add(cover)

Gada.scale(.65)

# green Areas

green_area = Rectangle(WIDTH/2, HEIGHT/2)
green_area.setFillColor(grass_color)
green_area.moveTo(WIDTH/4, HEIGHT - 300)
world.add(green_area)

green_area2 = green_area.clone()
green_area2.moveTo(WIDTH/4 + WIDTH/2, HEIGHT-300)
world.add(green_area2)

admin_building = Layer()
upp = Polygon(
    Point(0, 0),
    Point(50, 0),
    Point(50, 10),
    Point(40, 15),
    Point(40, 24),
    Point(10, 24),
    Point(10, 14),
    Point(0, 14)
)
upp.setFillColor("pink")
upWindow = Rectangle(25, 5)
upWindow.setFillColor("lightblue")
upWindow.setBorderWidth(0)
upWindow.moveTo(25, 8)
building = Polygon(
    Point(0, 0),
    Point(50, 0),
    Point(50, 10),
    Point(40, 15),
    Point(40, 24),
    Point(60, 50),
    Point(65, 75),
    Point(65, 90),
    Point(60, 90),
    Point(0, 90),
    Point(-15, 90),
    Point(-15, 65),
    Point(-10, 50),
    Point(10, 24),
    Point(10, 14),
    Point(0, 14),
    Point(0, 0)
)

building.setFillColor("grey")


building_dor = Rectangle(10, 20)
building_dor.setFillColor("blue")
building_dor.moveTo(25, 80)

bt = Text("Admin Building", 7)
bt.moveTo(25, 50)


admin_building.scale(2)
admin_building.moveTo(50, 10)
admin_building.add(building)
admin_building.add(upp)
admin_building.add(upWindow)
admin_building.add(building_dor)
admin_building.add(bt)
world.add(admin_building)


# main road
main_road = Rectangle(WIDTH, 150)
main_road.setFillColor(asphalt_color)
main_road.moveTo(WIDTH/2, HEIGHT-75)


# school road
school_road = Polygon(Point(WIDTH/2 - 220, HEIGHT), Point(WIDTH/2 - 80, 0),
                      Point(WIDTH/2 + 50, 0), Point(WIDTH/2 + 150, HEIGHT))
school_road.setFillColor(asphalt_color)


# side Roads

left_side_road = Polygon(
    Point(WIDTH/2 - 180, HEIGHT),
    Point(WIDTH/2 - 400, HEIGHT),
    Point(WIDTH/2 - 90, 0),
    Point(WIDTH/2 - 50, 0)
)

left_side_road.setFillColor(side_road_color)

right_side_road = Polygon(
    Point(WIDTH/2 + 150, HEIGHT),
    Point(WIDTH/2 + 400, HEIGHT),
    Point(WIDTH/2 + 60, 0),
    Point(WIDTH/2 + 50, 0)
)

right_side_road.setFillColor(side_road_color)

world.add(left_side_road)
world.add(right_side_road)
world.add(school_road)

# Trees

# on the road

for i in range(1, 8):
    t = create_tree(WIDTH/2 - 15, i*50, 0.5 + i*0.2)
    world.add(t)

# Light Poles

# for i in range(0, 5):
#     p = create_light(WIDTH/2 - (i*40), i*100, (i+1)*0.3)
#     world.add(p)

# Walls

wall_down = Rectangle(280, 100)
wall_down.setFillColor("brown")
wall_down.moveTo(125, HEIGHT/2 + 160)

world.add(wall_down)

world.add(Gada)
world.add(main_road)
