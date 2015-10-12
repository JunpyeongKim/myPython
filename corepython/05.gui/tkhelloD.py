#!/usr/bin/env python
# encoding=utf-8

# tkhelloD.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.3.4 Label, Button, and Scale Widgets
#   - Example 5-4. Label, Button, and Scale Demonstration
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloD.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloD3.py

from Tkinter import *


def resize(env=None):
    label.config(font='Helvetica -%d bold' % (scale.get()))

top = Tk()
top.geometry('250x150')

label = Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack()

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='red')
quit.pack()

mainloop()
