# encoding=utf-8

# function_docstring.py

# 10.8. DocStrings
# - http://www.swaroopch.com/notes/python/#docstrings
#   - documentation strings, its shorter name docstrings.
#   - Amazingly, we can even get the docstring back, when actually running.
#   - The pydoc command
#       - comes with your Python distribution
#       - works similarly to help() using docstrings


def print_max(x, y):
    # The convention
    # - a multi-line string
    #   - the first line starts with a capital letter and ends with a dot.
    #   - the second line is blank.
    #   - any detailed explanation starting from the third line.
    '''Prints the maximum of the numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print_max(3, 5)

# Python treats everything as an object.
# - using the __doc__ attribute of the function.
print print_max.__doc__
