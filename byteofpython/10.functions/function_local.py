# encoding=utf-8

# function_local.py

# 10.2. Local Variables
# - http://www.swaroopch.com/notes/python/#local_variables

# declared in the main block.
# - unaffected by the local assignment.
x = 50


def func(x):
    print 'x is', x
    # All variables have the scope of the block they are declared
    # in starting from the point of definition of the name.
    # - x is local
    x = 2
    print 'Changed local x to', x

func(x)
print 'x is still', x
