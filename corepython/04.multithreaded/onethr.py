#!/usr/bin/env python
# encoding=utf-8

# onethr.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.3.4 Life Without Threads
#   - Example 4-1. Loops Executed by a Single Thread
#       - If we were to execute loop0() and loop1() sequentially in a one process or
#         single-threaded program,
#         the total execution time would be at least 6 seconds.


from time import sleep, ctime


def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()


def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()


def main():
    print 'starting at:', ctime()
    loop0()
    loop1()
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()
