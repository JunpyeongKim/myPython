__author__ = '1000938'

import os

# Implementation.1
"""
def search(dirname):
    flist = os.listdir(dirname)
    for f in flist:
        next = os.path.join(dirname, f)
        if os.path.isdir(next):
            search(next)
        else:
            doFileWork(next)


def doFileWork(filename):
    # sp = os.path.splitext(filename)
    ext = os.path.splitext(filename)[-1]
    if ext == '.py': print(filename)

search('/Users/1000938/prj/python')
# """

# Implementation.2
# """
for (path, dir, files) in os.walk("/Users/1000938/prj/python"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print("%s/%s" % (path, filename))
# """