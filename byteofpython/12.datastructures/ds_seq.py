# encoding=utf-8

# ds_seq.py

# 12.5. Sequence
# - http://www.swaroopch.com/notes/python/#sequence
#   - lists, tuples, and strings
#   - major features
#       1. membership tests (i.e. in / not in)
#       2. indexing operators
#       3. slicing
#   - The great thing about sequences is that
#       - you can access tuples, lists, strings all in the same way.

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
print 'Character 0 is', name[0]

# The slicing operation by a colon --> [start:end:step]
#   - start, end, step : optional
#   - by default, the step size is 1
# Slicing on a list #
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is ', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]

# Slicing on a string #
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]
