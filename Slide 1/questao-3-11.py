import turtle
wn = turtle.Screen()
wn.bgcolor("white")
tess = turtle.Turtle()
tess.shape("blank")

for i in range(5):
    tess.forward(100) # Move tess along
    tess.right(144)  # ... and turn her

wn.mainloop()