
# To run the file: py -3.10 "C:\Users\Prashant\Desktop\Codingal1\Codingal\Module10\Lesson52\TkinterRelief.py"

from tkinter import *

window = Tk()
window.title("frame widget with relief")
window.geometry('300x200')

borderEffects = [FLAT, SUNKEN, RAISED, GROOVE, RIDGE]

for i in borderEffects:
    frame = Frame(master = window, relief = i, borderwidth = 5)
    frame.pack(side = LEFT)
    label = Label(master = frame, text = i)
    label.pack()

window.mainloop()