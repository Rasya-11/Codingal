# Make sure you add the image in your folder

# Import all the necessary libraries
from tkinter import *
from PIL import Image, ImageTk

# PIL (Python Imaging Library) provides image editing capabilities to the python interpreter

# Create a window with a title bar and set its geometry as well
root = Tk()
root.title("Image")
root.geometry("750x750")

# Now use Image.open to open and identify the given image file.
upload = Image.open("Img2.png")

# Convert this Image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image = image, height = 600, width = 600)
label.place(x = 50, y = 0)
label2 = Label(root, text = "Here is an image in Tkinter.")
label2.place(x = 220, y = 620)

# Run the application
root.mainloop()