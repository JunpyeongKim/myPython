# function_global.py
# 10.3. The global statement
# - http://www.swaroopch.com/notes/python/#the_global_statement

x = 50


def func():
    # makes it amply clear that the variables is defined in an outermost block.
    global x

    print 'x is ', x
    x = 2
    print 'Changed global x to', x

func()
print 'Value of x is', x
