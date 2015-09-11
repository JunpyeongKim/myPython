# encoding=utf-8

# function_keyword.py

# 10.5. Keyword Arguments
# - http://www.swaroopch.com/notes/python/#keyword_arguments


def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c

# use the name (keyword) instead of the position
# - not need to worry about the order of the argument.
func(3, 7)
func(25, c=23)
func(c=50, a=100)
