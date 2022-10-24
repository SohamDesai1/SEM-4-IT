from tkinter import *


def gettext():
    get = text.get(1.0, END)
    l1.config(text="You entered: " + get)


root = Tk()
root.geometry("400x300")
f1 = Frame(root, relief=SUNKEN)
f1.pack(side=LEFT, anchor=N)
text = Text(f1, width=30, height=10, bg="yellow")
text.pack(side=LEFT, anchor=N)
l1 = Label(f1, text="")
l1.pack(side=BOTTOM, anchor="sw")
b1 = Button(f1, text="Get Text", command=gettext)
b1.pack()
r = Radiobutton(f1, text="hello", value=1)
r.pack()
root.mainloop()
