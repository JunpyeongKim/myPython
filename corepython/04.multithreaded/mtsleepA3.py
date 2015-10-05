#!/usr/bin/env python
# encoding=utf-8

# mtsleepA3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.4 The thread Module
#   - Example 4-2. Using the thread Module
#       - onethr.py + thread
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepA3.py


from time import sleep, ctime
import _thread


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


# start_new_thread(function, args, kwargs=None)
def main():
    print('starting at:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)  # used as our synchronization mechanism. --> not reliable.
    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
