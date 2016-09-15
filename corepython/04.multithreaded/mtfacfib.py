#!/usr/bin/env python
# encoding=utf-8

# mtfacfib.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.6 Comparing Single vs. Multithreaded Execution
#   - Example 4-8. Fibonacci, Factorial, Summation
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtfacfib.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/mtfacfib3.py

from myThread import MyThread
from time import ctime, sleep


def fib(x):
    sleep(0.005)
    if x < 2: return 1

    return (fib(x-2) + fib(x-1))


def fac(x):
    sleep(0.1)
    if x < 2: return 1

    return (x * fac(x-1))


def sum(x):
    sleep(0.1)
    if x < 2: return 1

    return (x + sum(x-1))


funcs = (fib, fac, sum)
n = 12


def main():
    nfuncs = range(len(funcs))

    print '*** SINGLE THREAD'
    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at:', ctime()

    print '\n*** MULTIPLE THREADS'
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].name, '.res:', threads[i].getResult()

    print 'all DONE'

if __name__ == '__main__':
    main()
