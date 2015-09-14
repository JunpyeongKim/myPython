# encoding=utf-8

# module_dir.py

# 11.5. The dir function
# - http://www.swaroopch.com/notes/python/#the_dir_function

import sys

print 'dir(sys):'
# get names of attributes in sys module
print dir(sys)
print ''

print 'dir()'
# get names of attributes for current module
print dir()
print ''

# create a new variable 'a'
a = 5
print 'dir() after creating \'a\''
print dir()
print ''

# delete/remove a nme
del a
print 'dir() after deleting/removing \'a\''
print dir()
