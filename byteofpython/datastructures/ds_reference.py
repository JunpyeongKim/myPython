# ds_reference.py
# 12.7. References
# - http://www.swaroopch.com/notes/python/#references


print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so I remove it from list
del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# Notice that both shoplist and mylist both print
# the same list without the 'apple' confirming that
# they point to the same object

print 'Copy by making a full slice'
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# Notice that now the two lists are different
