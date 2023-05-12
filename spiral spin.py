from turtle import *

from random import *

chandra = Turtle(shape="turtle")

chandra.speed("fastest")

COLORS = ["orange", "blue", "red", "green", "purple"]

def draw_characterpart1():
    for i in range(36):
        for i in range(3):
            chandra.color(choice(COLORS))
            chandra.forward(80)
            chandra.right(120)

        chandra.left(10)

def draw_characterpart2():
    for i in range(36):
        for i in range(4):
            chandra.color(choice(COLORS))
            chandra.forward(70)
            chandra.right(90)
        chandra.left(10)

def draw_spiral():
    for i in range(10, 90, 10):
        chandra.color(choice(COLORS))
        chandra.circle(i, 180)

draw_characterpart1()

draw_characterpart2()

draw_spiral()

mainloop()