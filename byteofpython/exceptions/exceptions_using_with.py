__author__ = 'Junpyeong Kim'


# exceptions_using_with.py
# 16.6. The with statement
# - http://www.swaroopch.com/notes/python/#with


poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

with open("poem.txt") as f:
    # always calls the thefile.enter()
    for line in f:
        print line,
    # always calls the thefile.exit()
    # - the code in a finally block should be taken care of automatically by the exit method.
