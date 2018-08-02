# -*- coding: utf-8 -*-
from tkinter import *
import pip
import sys
import subprocess

reqs = subprocess.check_output([sys.executable,'-m','pip','list'])
installed_packages = reqs.decode("utf-8").split("\r\n")

app =Tk()

label = Label(text='Python Packages',font=('A',20,'bold'))
label.pack()

listbox = Listbox(bg='#f2f2f2',fg='red')
listbox.pack(fill=BOTH,expand=True)
for i in installed_packages:
    listbox.insert(END,i)

app.mainloop()
