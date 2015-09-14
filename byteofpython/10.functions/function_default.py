# encoding=utf-8

# function_default.py

# 10.4. Default Argument Values
# - http://www.swaroopch.com/notes/python/#default_argument_values


# can specify default argument values for parameters by '='.
# - should be a constant. More precisely, should be immutable.
# - Only those parameters that are at the end of the parameter list.
def say(message, times=1):
    print message * times

say('Hello')
say('World', 5)
