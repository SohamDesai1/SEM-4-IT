from tkinter import *

root = Tk()
root.geometry("800x600")
label = Label(root,
              text="""Web3 (also known as Web 3.0[1][2][3] and sometimes stylized as web3[4]) is an idea for a new 
              iteration of the World Wide Web based on blockchains, which incorporates concepts including 
              decentralization and token-based economics.[5] Some technologists and journalists have contrasted it 
              with Web 2.0, wherein they say data and content are centralized in a small group of companies sometimes 
              referred to as "Big Tech".[6] The term was coined in 2014 by Ethereum co-founder Gavin Wood, 
              and the idea gained interest in 2021 from cryptocurrency enthusiasts, large technology companies, 
              and venture capital firms.[6][7]""", justify=LEFT, font=("Helvetica", 10), bg="white", fg="black",
              padx=10, pady=10)

label.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()
