#!/usr/bin/env python
# encoding=utf-8

# pfaGUI3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.3.5 Partial Function Application Example
#   - Example 5-5. Road Signs PFA GUI Application
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/pfaGUI.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/pfaGUI3.py


from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'info'  #'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU
}

critCB = lambda : showerror('Error', 'Error Button Pressed!')
warnCB = lambda : showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda : showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')

Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
InfoButton = pto(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (
        signType.title(), eachSign,
        '.upper()' if signType == CRIT else '.title()')
    eval(cmd)


top.mainloop()
