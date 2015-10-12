#!/usr/bin/env python
# encoding=utf-8

# tkhelloC.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.3.3 The Label and Button Widget
#   - Example 5-3. Label and Button Widget Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloC.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloC3.py

import Tkinter


top = Tkinter.Tk()

hello = Tkinter.Label(top, text='Hello World!')
hello.pack()

quit = Tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
# The fill parameter tells it to let the QUIT button take
# up the rest of the horizontal real estate,
# and the expand parameter directs it to visually fill out the entire horizontal landscape,
# stretching the button to the left and right sides of the window.
# ==> Horizontal placement requires creating a new Frame object
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()
