#!/usr/bin/env python
# encoding=utf-8

# animalTtk3.pyw

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.4.5 Tile/Ttk
#   - Example 5-11. Tile/Ttk GUI Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalTtk.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalTtk3.py


from tkinter import Tk, Spinbox
from tkinter.ttk import Style, Label, Button, Combobox

top = Tk()
Style().configure("TButton",
    foreground='white', background='red')

Label(top,
    text='Animals (in pairs; min: pair, '
    'max: dozen)').pack()
Label(top, text='Number:').pack()

Spinbox(top, from_=2, to=12,
    increment=2, font='Helvetica -14 bold').pack()

Label(top, text='Type:').pack()

Combobox(top, values=('dog',
    'cat', 'hamster', 'python')).pack()

Button(top, text='QUIT',
    command=top.quit, style="TButton").pack()

top.mainloop()
