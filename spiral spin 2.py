from turtle import Screen, Turtle
from itertools import cycle

COLORS = ["orange", "blue", "red", "green", "purple"]

def draw_character():
    color = cycle(COLORS)

    for _ in range(36):
        for _ in range(3):
            chandra.color(next(color))
            chandra.forward(80)
            chandra.right(120)

        chandra.left(10)

    for _ in range(36):
        for _ in range(4):
            chandra.color(next(color))
            chandra.forward(70)
            chandra.right(90)

        chandra.left(10)

    for radius in range(10, 90, 10):
        chandra.color(next(color))
        chandra.circle(radius, 180)

screen = Screen()
screen.tracer(False)

chandra = Turtle()

for angle in range(720):
    chandra.reset()
    chandra.hideturtle()
    chandra.left(angle)
    draw_character()
    screen.update()

screen.tracer(True)
screen.mainloop()