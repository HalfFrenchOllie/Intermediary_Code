import turtle
import time
import random

x = 2
colours = ["Red", "orange", "yellow", "green", "blue", "indigo", "violet"]

while x < 10:
    tur = turtle.Turtle()
    tur.color(random.choice(colours))
    tur.shape ('circle')
    turtle.Screen().bgcolor("white")
    tur.speed (5)
    for i in range (x):
        tur.forward (100)
        tur.left (360.0/x)

        time.sleep(0.1)


    x = x + 1
