import turtle

# Setup screen
s = turtle.Screen()
s.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed("fast")
t.pensize(3)

# Function to draw equilateral triangle
def draw_triangle():
    t.color("white", "red")  # outline, fill
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

# Function to draw rectangle
def draw_rectangle():
    t.color("white", "blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()

# Function to draw hexagon
def draw_hexagon():
    t.color("white", "green")
    t.begin_fill()
    for _ in range(6):
        t.forward(80)
        t.left(60)
    t.end_fill()

# Draw triangle
t.penup()
t.goto(-200, 0)
t.pendown()
draw_triangle()

# Draw rectangle
t.penup()
t.goto(0, 0)
t.pendown()
draw_rectangle()

# Draw hexagon
t.penup()
t.goto(200, 0)
t.pendown()
draw_hexagon()

# Finish
turtle.done()