import turtle

while True:
    tur = turtle.Turtle()
    tur.color ('blue')
    tur.speed (1)


    Side = int(input("enter amount of side to the shape you want:"))
    for i in range (Side):
        tur.forward (100)
        tur.left (360.0/Side) #left is up
