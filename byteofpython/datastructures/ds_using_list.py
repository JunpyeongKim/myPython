# ds_using_list.py
# 12.1. List & 12.2. Quick Introduction To Object And Classes
# - http://www.swaroopch.com/notes/python/#list
#   - Data structures are used to store a collection of related data.
# - http://www.swaroopch.com/notes/python/#_quick_introduction_to_objects_and_classes
#   - List
#       - holds an ordered collection of items.
#       - is a mutable data type.
#   - help(list)

# This is my shopping list
# - can add any kind of object to a list.
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist), 'items to purchase'

print 'These items are:',
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist

print 'I will sort my list now'
# affects the list itself.
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist