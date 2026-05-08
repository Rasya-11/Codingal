# Write a Python program to - create a Tkinter window, set title to it, and set its geometry. 
# Then create a Tkinter grid of three rows and three columns, 
# add Labels as widgets and also add padding.

# To run the file: py -3.10 "C:\Users\Prashant\Desktop\Codingal1\Codingal\Module10\Lesson52\Tkinter2.py"


import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
        frame.grid(row = i, column = j, padx = 5, pady = 5)
        label = tk.Label(master = frame, text = f"row {i}\n column {j}")
        label.pack()

window.mainloop()