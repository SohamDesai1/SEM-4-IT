from tkinter import *

root = Tk()
root.geometry("300x300")
canvas = Canvas(root, width=200, height=100)
canvas.pack()
canvas.create_line(0, 10, 200, 100)
canvas.create_line(0, 100, 200, 10, fill="red", dash=(4, 4))
canvas.create_rectangle(50, 25, 150, 75, fill="blue")
canvas.create_oval(80, 35, 150, 75, fill="yellow")
canvas.create_text(100, 50, text="Hello", fill="green")
canvas.create_polygon(100, 100, 150, 100, 150, 50, fill="red")
root.mainloop()
