import tkinter as tk
from MailOperations import MailOperations
from Page import Page


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        file = ""

        messages = MailOperations("testosipciuc1@gmail.com", "!TestOsipciuc1").read_mail()
        print(messages)

        label = tk.Text(self, width="80", height="35")
        label.insert(tk.END, messages)
        label.pack(expand=True)
