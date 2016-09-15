#!/usr/bin/env python
# encoding=utf-8

# mtsleepF.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.7.3 Locking Example
#   - Example 4-10. Locks and More Randomness
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepF.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepF3.py


from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print '[%s] Started %s' % (ctime(), myname)  #print '[{0}] Started {1}'.format(ctime(), myname)
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print '[%s] Completed %s (%d secs)' % ( #print '[{0}] Completed {1} ({2} secs)'.format(
        ctime(), myname, nsec)
    print '    (remaining: %s)' % (remaining or 'NONE') #print '    (remaining: {0})'.format(remaining or 'NONE')
    lock.release()


def _main():
    for pause in loops:
        print 'Thread.start()...pause:', pause
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    _main()
