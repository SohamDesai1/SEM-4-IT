from tkinter import *

root = Tk()
root.title("Scrollbar")
root.geometry("600x600")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()
