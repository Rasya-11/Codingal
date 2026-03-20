# Set the screen for turtle graphics, including its size and title Set the screen colour as per your choice
# Create a star using turtle

import turtle

turtle.Screen().bgcolor("Orange")
board = turtle.Turtle()

#first triangle
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)
board.pendown()
board.right(90)

#second triangle
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()