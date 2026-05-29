from tkinter import *
import random
import string

window = Tk()
window.title("Password Generator")
window.geometry("300x250")

def password():
    characters = string.ascii_letters + string.digits + string.punctuation
    
    result = ""
    
    for i in range(12):
        result += random.choice(characters)

    entry.delete(0, END)
    entry.insert(0, result)

label = Label(window, text="Random Password Generator")
label.pack(pady=10)

entry = Entry(window, width=25)
entry.pack(pady=10)

button = Button(window, text="Generate Password", command=password)
button.pack(pady=10)

frame = Frame(window, relief=RAISED, borderwidth=3)
frame.pack(pady=10)

frame_label = Label(frame, text="Includes letters,\nnumbers and symbols")
frame_label.pack()

textbox = Text(window, height=3, width=30)
textbox.insert(END, "Click the button to generate.")
textbox.pack(pady=10)

window.mainloop()