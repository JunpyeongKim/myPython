# encoding=utf-8

# exceptions_raise.py

# 16.4. Raising Exceptions
# - http://www.swaroopch.com/notes/python/#_raising_exceptions


# our own exception type
# - must be a derived class of the Exception class.
class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = raw_input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work can continue as usual here
except EOFError:    # ctrl+d
    print 'Why did you do an EOF on me?'
# as "the corresponding errors/exceptions object"
# - analogous to parameters and arguments in a function call
except ShortInputException as ex:
    print ('ShortInputException: The input was ' + \
           '{0} long, expected at least {1}')\
        .format(ex.length, ex.atleast)
else:
    print 'No exception was raised.'

'''
    $ python exceptions_raise.py
    Enter something --> a
    ShortInputException: The input was 1 long, expected at least 3

    $ python exceptions_raise.py
    Enter something --> abc
    No exception was raised.
'''
