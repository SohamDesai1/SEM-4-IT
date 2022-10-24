from tkinter import *

root = Tk()
root.geometry("300x300")
f1 = Frame(root, width=200, height=200, bg='red', relief=SUNKEN, borderwidth=5)
f1.pack(side=LEFT, fill=Y)
l1 = Label(f1, text='Hello', bg='red',font = "Helvetica 10 bold")
l1.pack(pady=42)
root.mainloop()
