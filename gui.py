from tkinter import *
import collections
from config import Config


class NetworkScanGui():

    def __init__(self, master):
        self.master = master
        self.master.title("Network Scan Configuration")

        self.entry_list = []
        self.label_texts = collections.OrderedDict([
            ("Database password:", Config.load('password')),
            ("Database username:", Config.load('user')),
            ("Host:", Config.load('host')),
            ("Database:", Config.load('database')),
            ("Mail username:", Config.load('mail_username')),
            ("Mail password:",  Config.load('mail_password')),
            ("Sender:",  Config.load('sender')),
            ("Receiver:",  Config.load('receiver')),
            ("Server:",  Config.load('server'))
        ])

        i = 0
        for button in self.label_texts:
            entry_value = StringVar()
            # entry_value.set("hello")
            entry_value.set(list(self.label_texts.items())[i][1])
            self.entry_list.append(entry_value)
            self.entry_list[i].trace("w", lambda name, index, mode, var=self.entry_list[i], i=i:
                                     self.change_entry(var, i))
            Label(master, text=button, padx=4, pady=4).grid(column=0, row=i, sticky=E)
            Entry(master, width=30, textvariable=self.entry_list[i]).grid(column=1, row=i)
            i += 1

    def change_entry(self, sv, i):
        Config.write(list(self.label_texts.items())[i][0], sv.get())

root = Tk()
gui = NetworkScanGui(root)
root.mainloop()
