# Write a Python program to - create a Tkinter window, set title to it, and set its geometry. 
# Then add these widgets to the window - Label, Button, Entry, Frame, and a Text box.

#To run the file: py -3.10 "C:\Users\Prashant\Desktop\Codingal1\Codingal\Module10\Lesson52\Tkinter1.py"

from tkinter import *

Window = Tk()
Window.title('Tkinter Sample Window')
Window.geometry('300x300')

greeting = Label(text = "Hello User!", fg = 'black', bg = 'white')
button = Button(text = "Click here", fg = 'white', bg = 'black')
entry = Entry(fg = 'yellow', bg = 'blue', width = '50')
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master = Window, relief = RAISED, borderwidth = 5)
frame.pack()
label = Label(master = frame, text = "sample frame")
label.pack()

textbox = Text(fg = 'green', bg = 'yellow')
textbox.pack()

Window.mainloop()