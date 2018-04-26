import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

size = 20
for j in [3, 4, 6, 8]:
    for i in range(j):
        tess.forward(100)  # Move tess along
        tess.left(360 / j)  # ... and turn her

wn.mainloop()