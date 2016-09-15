#!/usr/bin/env python
# encoding=utf-8

# animalPmw.pyw

# Core Python Application Programming 3E, Wesley J. Chun
# - 5.4.2 Python MegaWidgets(PMW)
#   - Example 5-8. Pmw GUI Demo
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalPmw.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch05/animalPmw3.py
#   - No Pmw


from Tkinter import Button, END, Label, W
from Pmw import initialise, ComboBox, Counter

top = initialise()

lb = Label(top,
    text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Counter(top, labelpos=W, label_text='Number:',
    datatype='integer', entryfield_value=2,
    increment=2, entryfield_validate={'validator':
    'integer', 'min': 2, 'max': 12})
ct.pack()

cb = ComboBox(top, labelpos=W, label_text='Type:')
for animal in ('dog', 'cat', 'hamster', 'python'):
    cb.insert(END, animal)
cb.pack()

qb = Button(top, text='QUIT',
    command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()
