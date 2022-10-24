from tkinter import *
from tkinter import messagebox as msg


def help():
    a = msg.showinfo("Help", "This is a help message.")


def rate():
    a = msg.askquestion("Rate", "How do you rate this program?")
    print("You rated this program:", a)


root = Tk()
root.geometry("500x500")
root.title("Menu")

mymenu = Menu(root)
m = Menu(mymenu, tearoff=0)
m.add_command(label="New", command=lambda: print("New"))
m.add_command(label="Open", command=lambda: print("Open"))
m.add_command(label="Save", command=lambda: print("Save"))
mymenu.add_cascade(label="File", menu=m)

m1 = Menu(mymenu, tearoff=0)
m1.add_command(label="Cut", command=lambda: print("Cut"))
m1.add_command(label="Copy", command=lambda: print("Copy"))
m1.add_command(label="Paste", command=lambda: print("Paste"))
mymenu.add_cascade(label="Edit", menu=m1)

m2 = Menu(mymenu, tearoff=0)
m2.add_command(label="Help", command=help)
m2.add_command(label="Rate us", command=rate)
mymenu.add_cascade(label="Help", menu=m2)

root.config(menu=mymenu)
root.mainloop()
