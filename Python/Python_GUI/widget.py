from tkinter import *

root = Tk()
root.geometry("500x400")
image = PhotoImage(file="Text.png")
label = Label(root, image=image)
label.place(x=0, y=0)

l1 = Label(root, text="username", padx=10, pady=10)
l2 = Label(root, text="password", padx=10, pady=10)
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

l1var = StringVar()
l2var = StringVar()

username = Entry(root, textvariable=l1var)
password = Entry(root, textvariable=l2var, show="*")
username.grid(row=0, column=2)
password.grid(row=1, column=2)
button = Button(root, text="Show Password", command=lambda: password.config(show=""), padx=5, pady=5)
login = Button(root, text="Login", command=lambda: print(l1var.get(), l2var.get()), padx=5, pady=5)
button.grid(row=2, column=1)
login.grid(row=2, column=2)

root.mainloop()
