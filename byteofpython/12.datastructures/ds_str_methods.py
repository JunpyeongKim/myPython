# encoding=utf-8

# ds_str_methods.py

# 12.8. More About Strings
# - http://www.swaroopch.com/notes/python/#more_strings
#   - help(str)

# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'

if 'a' in name:
    print 'Yes, it contains the string "a"'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
