#!/usr/bin/env python
# encoding=utf-8

# tkhelloC3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.3.3 The Label and Button Widget
#   - Example 5-3. Label and Button Widget Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloC.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/tkhelloC3.py

import tkinter


top = tkinter.Tk()

hello = tkinter.Label(top, text='Hello World!')
hello.pack()

quit = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
