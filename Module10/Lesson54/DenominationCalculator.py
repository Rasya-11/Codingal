from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("C:\\Users\\Prashant\\Desktop\\Codingal1\\Codingal\\Module10\\Lesson54\\Cash Tally Img.jpg")
upload = upload.resize((300, 300))

# Convert this Image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image = image, bg = "light blue")
label.place(x = 180, y = 20)
label1 = Label(root, text = "Welcome to Denomination Calculator.", bg = "light blue")
label1.place(relx = 0.5, y = 340, anchor = CENTER)

def msg():
    msgbox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if msgbox == "ok":
        topWin()
        
button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white') 
button1.place(x=260, y=360)

def topWin():
    top = Toplevel(root)
    top.title('Currency Denomination Counter')
    top.configure(bg='Grey')
    top.geometry('600x400')
    label = Label(top, text = "Enter Total Amount", bg = "light grey")
    entry = Entry(top)
    lbl = Label(top, text = "Here are the number of notes for each denomination.", bg = "light grey")
    l1 = Label(top, text="50", bg="light grey")
    l2 = Label(top, text="20", bg="light grey")
    l3 = Label(top, text="10", bg="light grey")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        amount = int(entry.get())
        notes50 = amount//50
        amount = amount%50
        notes20 = amount//20
        amount = amount%20
        notes10 = amount//10
        amount = amount%10
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t1.insert(END, str(notes50))
        t2.insert(END, str(notes20))
        t3.insert(END, str(notes10))
    
    btn = Button(top, text = "calculate", command = calculator, bg = "brown", fg = "white")

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()

root.mainloop()

