# module_using_sys.py
# 11. Modules
# - http://www.swaroopch.com/notes/python/#module


import sys
import os

print ('The command line arguments are:')
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'

print os.getcwd()

'''
    $ python module_using_sys.py we are arguments
'''