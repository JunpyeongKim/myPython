# module_using_name.py
# 11.3. A module's name
# - http://www.swaroopch.com/notes/python/#module_name


# the name attribute of the module
# - being used by itself or
# - being imported from another module
if __name__ == '__main__':
    print 'This program is being run by itself'
else:
    print 'I am being imported form another module'

'''
    $ python module_using_name.py
    This program is being run by itself

    $ python
    >>> import module_using_name
    I am being imported from another module
'''