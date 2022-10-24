import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.minsize(200, 300)
root.maxsize(1200, 1000)

root.title("Demo")
root.label = tk.Label(root, text="Hello World")
root.label.pack()
root.tk.mainloop()
 