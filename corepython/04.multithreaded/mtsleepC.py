#!/usr/bin/env python
# encoding=utf-8

# mtsleepC.py

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
#   - Create Thread Instance, Passing in Function
#       - Example 4-4. Using the threading Module
#           - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepC.py
#           - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepC3.py



import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:    # start threads
        threads[i].start()

    for i in nloops:    # wait for all
        threads[i].join()   # threads to finish

    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()
