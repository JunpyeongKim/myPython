#!/usr/bin/env python
# encoding=utf-8

# mtsleepB3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.4 The thread Module
#   - Example 4-3. Using thread and Locks
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepB3.py

from time import sleep, ctime
import _thread


loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()


def main():
    print('starting threads...')
    locks = []
    nloops = list(range(len(loops)))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
