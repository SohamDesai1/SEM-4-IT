from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Brokerage Calculator")
root.geometry("400x300")

qau = tk.DoubleVar()
bu = tk.DoubleVar()
se = tk.DoubleVar()
stock = tk.StringVar()
Stock = Entry(root, textvariable=stock, width=10)
quantity = Entry(root, textvariable=qau, width=10)
buy = Entry(root, textvariable=bu, width=10)
sell = Entry(root, textvariable=se, width=10)
quantity.grid(row=1, column=1)
buy.grid(row=2, column=1)
sell.grid(row=3, column=1)
Stock.grid(row=0, column=1)


def newWindow():
    newwin = Toplevel(root)
    newwin.title("Brokerage Calculator")
    newwin.geometry("700x250")
    q = float(quantity.get())
    b = float(buy.get())
    s = float(sell.get())
    total_buy = q * b
    total_sell = q * s
    b1 = (0.05 / 100) * total_sell
    b2 = 20
    brokerage = 0
    if b1 > b2:
        brokerage = b2 * 2
    else:
        brokerage = b1 * 2
    stt = total_sell * (0.025 / 100)
    sd = total_buy * (0.003 / 100)
    etc = (total_buy * (0.00345 / 100)) + (total_sell * (0.00345 / 100))
    SEBI = (total_buy * (0.0001 / 100)) + (total_sell * (0.0001 / 100))
    GST = ((18 / 100) * brokerage) + ((18 / 100) * etc)
    total_c = brokerage + stt + sd + etc + SEBI + GST
    total = ((s - b) * q) - total_c
    Label(newwin, font="Arial", text="For Stock: " + str(Stock.get())).grid(row=5, column=4)
    Label(newwin, font="Arial", text="Total Charges: " + str(total_c)).grid(row=5, column=1, sticky=W)
    Label(newwin, font="Arial", text="Total Profit: " + str(total)).grid(row=6, column=4)
    Label(newwin, font="Arial", text="Brokerage: " + str(brokerage)).grid(row=6, column=1, sticky=W)
    Label(newwin, font="Arial", text="Settlement Charges: " + str(stt)).grid(row=7, column=1, sticky=W)
    Label(newwin, font="Arial", text="Stamp Duty: " + str(sd)).grid(row=8, column=1, sticky=W)
    Label(newwin, font="Arial", text="Exchange Charges: " + str(etc)).grid(row=9, column=1, sticky=W)
    Label(newwin, font="Arial", text="SEBI Charges: " + str(SEBI)).grid(row=10, column=1, sticky=W)
    Label(newwin, font="Arial", text="GST: " + str(GST)).grid(row=11, column=1, sticky=W)


Label(root, font="Arial", text="Stock").grid(row=0, column=0, sticky=W)
Label(root, font="Arial", text="Quantity").grid(row=1, column=0, padx=5, pady=15, sticky=W)
Label(root, font="Arial", text="Buy Price").grid(row=2, column=0, padx=5, pady=15, sticky=W)
Label(root, font="Arial", text="Sell Price").grid(row=3, column=0, padx=5, pady=15, sticky=W)
Button(root, font="Arial", text="Submit", command=newWindow).grid(row=5, column=5, padx=5, pady=15, sticky=W)

root.bind('<Return>', lambda event: newWindow())
root.mainloop()
