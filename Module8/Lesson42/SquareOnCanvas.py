# Write a Python program to set the screen size, colour and title for turtle graphics 
# and draw a square using turtle.

import turtle
import tkinter

print("Tkinter works!")

turtle.Screen().bgcolor("Orange")
sc = turtle.Screen()
sc.setup(400,300) #width = 400px, height = 300px
turtle.title("Welcome to turtle window!")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1
    