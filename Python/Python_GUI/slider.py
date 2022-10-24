from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Slider")

mySlider = Scale(root, from_=0, to=100, orient=HORIZONTAL,tickinterval=10, length=400, showvalue=0)
mySlider.set(50)
mySlider.pack()

root.mainloop()
