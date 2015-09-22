# encoding=utf-8

# io_pickle.py

# 15.3. Pickle
# - http://www.swaroopch.com/notes/python/#pickle


import pickle
# a standard module.
# - store any plain Python object in a file and then get it back later.

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')

# Dump the object to a file --> pickling
pickle.dump(shoplist, f)
f.close()

print 'before dumping, shoplist: ', shoplist

del shoplist

try:
    print 'after dumping, shoplist: ', shoplist
except NameError:
    print 'deleted shoplist'

# Read back from the storage
f = open(shoplistfile, 'rb')

# Load the object from the file --> unpickling
storedlist = pickle.load(f)

# f.close()   # ???
print 'after loading, storedlist:', storedlist
