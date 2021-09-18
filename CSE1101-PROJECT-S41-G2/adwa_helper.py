from cs1graphics import *
from configuration import *
from time import sleep


def create_sun(color, radius):
    sun = Circle(radius)
    sun.setFillColor(color)
    sun.setBorderWidth(0)
    sun.moveTo(800, 400)
    return sun


def soldier_move(soldier, weapon, x, y, shield=None):
    soldier.soldier.move(x, y)
    if weapon:
        weapon.weapon.move(x, y)
    if shield:
        shield.shield.move(x, y)


def fade_in(t, textcolor=list(sun_color)):
    textcolor = list(sun_color)
    for k in range(200):
        for j in range(len(textcolor)):
            if textcolor[j] > 0:
                textcolor[j] -= 1
        t.setFontColor(tuple(textcolor))
        sleep(.005)


def fade_out(t, textcolor):
    for k in range(200):
        for j in range(len(textcolor)):
            if textcolor[j] < 255:
                textcolor[j] += 1
        t.setFontColor(tuple(textcolor))
        sleep(.005)
