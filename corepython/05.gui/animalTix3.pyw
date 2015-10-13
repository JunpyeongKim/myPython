#!/usr/bin/env python
# encoding=utf-8

# animalTix3.pyw

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.4.1 Tk Interface eXtensions (Tix)
#   - Example 5-7. Tix GUI Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalTix.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalTix3.py
#   - Not work

from tkinter import Label, Button, END
from tkinter.tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')

lb = Label(top,
    text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Control(top, label='Number:',
    integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack()

cb = ComboBox(top, label='Type:', editable=True)
for animal in ('dog', 'cat', 'hamster', 'python'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='QUIT',
    command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()

