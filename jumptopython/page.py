__author__ = 'Junpyeong Kim'

import sys


# page.py


def usage():
    print("Usage: python %s total items-a-page" % sys.argv[0])


def getPage(m, n):
    page, remainder = divmod(m, n)
    if remainder > 0:
        page += 1
    return page


try:
    total = int(sys.argv[1])
    items_a_page = int(sys.argv[2])
except IndexError:
    usage()
    sys.exit(2)


print("""
Total : %s
Items a Page : %s
Pages(required) : %d
""" % (total, items_a_page, getPage(total, items_a_page)) )