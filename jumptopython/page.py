__author__ = '1000938'

import sys


def usage():
    print("Usage: python %s total numinpage" % sys.argv[0])

def getPage(m, n):
    page, remainder = divmod(m, n)
    if remainder > 0:
        page += 1
    return page

print("""
Total : %s
Numer in a Page : %s
Pages : %d
""" % (sys.argv[1], sys.argv[2], getPage(int(sys.argv[1]), int(sys.argv[2])))
      )
