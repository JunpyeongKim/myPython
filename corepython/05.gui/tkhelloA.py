#!/usr/bin/env python
# encoding=utf-8

# tkhelloA.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.3.1 Label Widget
#   - Example 5-1. Label Widget Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloA.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloA3.py
#       - the Tkinter version of “Hello World!”

import Tkinter


top = Tkinter.Tk()
label = Tkinter.Label(top, text='Hello World!')
label.pack()
Tkinter.mainloop()
