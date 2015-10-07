#!/usr/bin/env python
# encoding=utf-8

# mtsleepE3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.5 The threading Module
#   - gives you not only a Thread class but also a wide variety of synchronization mechanisms
#   - The Thread() class also contains a form of synchronization, so explicit use of locking primitives is not necessary.
#   - (*) Daemon Thread
#       - the thread module does not support the concept of daemon (or daemonic) threads.
#       - Support for daemon threads is available in the threading module.
#       - thread.daemon = True
#       - A new child thread inherits its daemonic flag from its parent.
#       - The entire Python program (read as: the main thread) will stay alive until all non-daemonic threads have exited
#
# - 4.5.1 The Thread Class
#   - create threads using the Thread class
#       - 1) passing in function <-- better
#       - 2) passing in callable class instance
#       - 3) Subclass Thread and create subclass instance <-- the best (a more object-oriented interface)
#   - Subclass Thread and Create Subclass Instance
#       - Example 4-6. Subclassing Thread
#           - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepE3.py
#       - compare the source between the mtsleepD and mtsleepE modules
#           - 1) our MyThread subclass constructor must first invoke the base class constructor
#           - 2) the former special method __call__() must be called run() in the subclass



import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        print('func:', func, ', args:', args, ', name:', name)
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('run:', self.args)
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = list(range(len(loops)))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
