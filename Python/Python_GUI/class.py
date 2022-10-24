from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI")
        self.geometry("500x500")

    def status(self, text):
        self.setvar("status", text)
        self.statusbar = Label(self, textvariable=self.status)
        self.statusbar.pack(side=BOTTOM, fill=X)
        self.statusbar.config(relief=SUNKEN, bd=1)

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
