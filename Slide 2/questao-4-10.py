import turtle

def draw_star(t, sz):
    """Make turtle t draw a star of sz."""
    for j in range(5):
        for i in range(5):
            t.forward(sz)  # Move tess along
            t.right(144)  # ... and turn her
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()


wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()  # Create alex
alex.shape("blank")
alex.pencolor("pink")
alex.pensize(4)
draw_star(alex, 100)  # Call the function to draw the square

wn.mainloop()