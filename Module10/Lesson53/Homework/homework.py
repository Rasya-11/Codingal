from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x650")
root.config(bg="lightblue")

player = 0
computer = 0

options = ["Rock", "Paper", "Scissors"]

rock = ImageTk.PhotoImage(Image.open("rock.png").resize((120,120)))
paper = ImageTk.PhotoImage(Image.open("paper.png").resize((120,120)))
scissors = ImageTk.PhotoImage(Image.open("scissors.png").resize((120,120)))

def game(choice):

    global player
    global computer

    comp = random.choice(options)

    if comp == "Rock":
        comp_img.config(image=rock)

    elif comp == "Paper":
        comp_img.config(image=paper)

    else:
        comp_img.config(image=scissors)

    if choice == comp:
        result = "Tie"

    elif choice == "Rock" and comp == "Scissors":
        result = "You Win"
        player += 1

    elif choice == "Paper" and comp == "Rock":
        result = "You Win"
        player += 1

    elif choice == "Scissors" and comp == "Paper":
        result = "You Win"
        player += 1

    else:
        result = "Computer Wins"
        computer += 1

    result_label.config(text=result)

    score.config(text="Player: " + str(player) + "   Computer: " + str(computer))

    messagebox.showinfo("Result", "You chose " + choice + "\nComputer chose " + comp)

title = Label(root, text="Rock Paper Scissors", font=("Arial",24,"bold"), bg="lightblue")
title.pack(pady=20)

frame = Frame(root, bg="lightblue")
frame.pack(pady=20)

Button(frame, image=rock, command=lambda: game("Rock")).grid(row=0,column=0,padx=20)
Button(frame, image=paper, command=lambda: game("Paper")).grid(row=0,column=1,padx=20)
Button(frame, image=scissors, command=lambda: game("Scissors")).grid(row=0,column=2,padx=20)

Label(root, text="Computer Choice", font=("Arial",18), bg="lightblue").pack()

comp_img = Label(root, bg="lightblue")
comp_img.pack(pady=10)

result_label = Label(root, text="Choose One", font=("Arial",18), bg="lightblue", fg="red")
result_label.pack(pady=20)

score = Label(root, text="Player: 0   Computer: 0", font=("Arial",16), bg="lightblue")
score.pack()

root.mainloop()