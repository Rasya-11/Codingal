
# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
def msg():
    messagebox.showwarning("Alert", "Virus found!")

# This will be called once the button is clicked

# messagebox.showwarning("Window Name", "Text to be displayed")

# Adding Button Widget to Window
button = Button(root, text = "Scan for virus.", command = msg)
button.place(x = 40, y = 80)

# Entering main event loop
root.mainloop()