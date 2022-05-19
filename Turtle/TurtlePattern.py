import turtle
import time

x = 3

while x < 10:
    tur = turtle.Turtle()
    tur.color ('blue')
    tur.speed (1)
    for i in range (x):
        tur.forward (100)
        tur.left (360.0/x)

        time.sleep(0.1)


    x = x + 1
