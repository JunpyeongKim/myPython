#!/usr/bin/env python
# encoding=utf-8

# myThread.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.5.1 The Thread Class
#   - MyThread + some diagnostic output + self.res + self.getResult()
#   - Example 4-7. MyThread Subclass of Thread
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/myThread3.py


import threading
from time import time, ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name='', verb=False):
        print('func:', func, ', args:', args, ', name:', name)
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.verb = verb

    def getResult(self):
        return self.res

    def run(self):
        print('run:', self.args, self.verb)
        if self.verb:
            print('starting', self.name, 'at:', ctime())

        self.res = self(*self.args)

        if self.verb:
            print(self.name, 'finished at:', ctime())

