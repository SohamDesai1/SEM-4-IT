from tkinter import *


def exit(event):
    root.destroy()


root = Tk()
root.geometry("200x200")
button = Button(root, text="Click Me")
button.pack()
button.bind("<Button-1>", lambda event: print("Left Click"))
button.bind("<Button-2>", lambda event: print("Middle Click"))
button.bind("<Button-3>", lambda event: print("Right Click"))
button.bind("<Double-1>", exit)

root.mainloop()
