from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("image")
root.geometry("400x400")
image = Image.open("Text.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack()

root.mainloop()
