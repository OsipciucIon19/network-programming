import tkinter as tk
from Page1 import Page1
from Page2 import Page2


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p1.config(bg="Gray")
        p2 = Page2(self)
        p2.config(bg="Gray")

        buttonbar = tk.Frame(self)
        container = tk.Frame(self)
        buttonbar.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonbar, text="Send E-Mail", command=p1.lift)
        b2 = tk.Button(buttonbar, text="View inbox", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()
