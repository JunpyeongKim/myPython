# encoding=utf-8

# function_param.py

# 10.1. Function Parameters
# - http://www.swaroopch.com/notes/python/#function_parameters


# the names given in a function definition are called "parameters".
# a and b : parameters
def print_max(a, b):
    if a > b:
        print a, 'is maximum'
    elif a == b:
        print a, 'is equal to ', b
    else:
        print b, 'is maximum'

# the values you supply in the function call are called "arguments".
# directly pass literal values.
# the numbers as arguments.
print_max(3, 4)

x = 5
y = 7

# pass variables as arguments.
# variables as arguments.
print_max(x, y)
