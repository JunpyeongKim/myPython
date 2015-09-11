# encoding=utf-8

# function_return.py

# 10.7. The return statement
# - http://www.swaroopch.com/notes/python/#the_return_statement


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print maximum(2, 3)


# None : a special type in Python. --> nothingness
# Every function implicitly contains a return None statement at the end.
def some_function():
    pass

print some_function()
