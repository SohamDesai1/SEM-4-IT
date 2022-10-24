from tkinter import *


def show():
    if checkbox1.get() == 1:
        print('Checkbox1 is checked')
    else:
        print('Checkbox1 is unchecked')


root = Tk()
root.geometry("300x300")
l1 = Label(root, text="checkbutton")
l1.pack(pady=10)
checkbox1 = IntVar()
checkbox = Checkbutton(root, text="checkbutton", variable=checkbox1)
checkbox.pack()
button = Button(root, text="click", command=show)
button.pack()

root.mainloop()
