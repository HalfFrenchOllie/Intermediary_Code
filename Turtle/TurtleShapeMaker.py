import turtle


tur = turtle.Turtle()
tur.color ('blue')
tur.speed (1)



print("number of side")

Side = int(input("amount:"))
for i in range (Side):
    tur.forward (100)
    tur.left (360.0/Side) #left is up
