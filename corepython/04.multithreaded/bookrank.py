#!/usr/bin/env python
# encoding=utf-8

# bookrank.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 4.7.1  Book Rankings Example
#   - Example 4-9. Book Rankings "Screenscraper"
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch04/bookrank.py

from atexit import register
from re import compile
from threading import Thread
from time import ctime
# from urllib2 import urlopen as uopen  # not work
from urllib import urlopen as uopen


'''
    http://www.amazon.com/dp/0132269937

    Amazon Best Sellers Rank: #201,253 in Books (See Top 100 in Books)
            #187 in Books > Computers & Technology > Programming > Languages & Tools > Python
            #585 in Books > Computers & Technology > Programming > Web Programming
            #891 in Books > Textbooks > Computer Science > Programming Languages

    ==>

    At Thu Oct  8 15:16:22 2015 on Amazon...
    - 'Python Web Development with Django' ranked 544,103
    - 'Python Fundamentals' ranked 2,765,760
    - 'Core Python Programming' ranked 201,253
'''

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}


def getRanking(isbn):
    page = uopen('%s%s' % (AMZN, isbn))  # '{0}{1}'.format(AMZN, isbn) for 2.6+
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print '- %r ranked %s' % (ISBNs[isbn], getRanking(isbn))


def _main():
    print 'At', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        Thread(target=_showRanking, args=(isbn,)).start()  #_showRanking(isbn)


@register
def _atexit():
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    _main()
