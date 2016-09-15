#!/usr/bin/env python
# encoding=utf-8

# mtsleepB.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.4 The thread Module
#   - Example 4-3. Using thread and Locks
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtsleepB.py
#   - the thread module only to introduce the reader to threaded programming.
#   - Your MT application should use higher-level modules such as the threading module,

from time import sleep, ctime
import thread


loops = [4, 2]


def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()


def main():
    print 'starting threads...'
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    # First, we wanted to synchronize the threads, so that all the horses started out the gate around the same time
    # and second, locks take a little bit of time to be acquired.
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # The final loop just sits and spins (pausing the main thread)
    # until both locks have been released before continuing execution.
    # Because we are checking each lock sequentially, we might be at the mercy of
    # all the slower loops if they are more toward the beginning of the set of loops.
    # When that lock is released, remaining locks may have already been unlocked
    # (meaning that corresponding threads have completed execution)
    for i in nloops:
        while locks[i].locked():
            pass

    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()
