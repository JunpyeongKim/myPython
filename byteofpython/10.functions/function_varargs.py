# encoding=utf-8

# function_varargs.py

# 10.6. VarArgs parameters
# - http://www.swaroopch.com/notes/python/#varargs_parameters


# any number of parameters by using the stars.
# - a starred parameter
#   - all the positional arguments are collected as a tuple.
# - a double-starred parameter
#   - all the keyword arguments are collected as a dictionary.
def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print total(10, 1, 2, 3, vegetables=50, fruits=100)
