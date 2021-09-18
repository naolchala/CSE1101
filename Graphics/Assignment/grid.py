"""
A Grid framework for CS1Graphics 
Developed By Naol Chala, 2021

The hardest thing in creating graphics project is positioning items in cordinates, and this is because there is no reference.
but, by including the grid module in our script we can get the reference Point

Usage
==========
importing
``from grid import Grid```
using
g = Grid(world, scale)

scale - the num of pixels between consequentive lines

"""

from cs1graphics import *


class Grid:
    def __init__(self, world, scale):
        self.grid = Layer()
        self.world = world
        self.world.add(self.grid)
        self.grid.setDepth(-2000)
        self.w = world.getWidth()
        self.h = world.getHeight()

        # vertical
        for i in range(self.w/scale):
            p = Path(
                Point(scale*i, 0),
                Point(scale*i, self.h)
            )
            p.setBorderColor("gray")
            t = Text("{}".format(scale*i), 7)
            t.moveTo(scale*i, 7)
            t2 = t.clone()
            t2.moveTo(scale*i, self.h - 7)
            self.grid.add(p)
            self.grid.add(t)
            self.grid.add(t2)
        # horizontal
        for i in range(self.h/scale):
            p = Path(
                Point(0, scale*i),
                Point(self.w, scale*i)
            )
            p.setBorderColor("gray")
            t = Text("{}".format(scale*i), 7)
            t.moveTo(7, scale*i)
            t2 = t.clone()
            t2.moveTo(self.w - 7, scale*i)
            self.grid.add(p)
            self.grid.add(t)
            self.grid.add(t2)
