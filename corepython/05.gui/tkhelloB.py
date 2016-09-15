#!/usr/bin/env python
# encoding=utf-8

# tkhelloB.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.3.2 Button Widget
#   - Example 5-2. Button Widget Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloB.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloB3.py

import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top, text='Hello World!', command=top.quit)
quit.pack()
Tkinter.mainloop()
