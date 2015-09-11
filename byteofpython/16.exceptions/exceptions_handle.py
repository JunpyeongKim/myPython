# encoding=utf-8

# exceptions_handle.py

# 16.3. Handling Exceptions
# - http://www.swaroopch.com/notes/python/#_handling_exceptions


try:
    # all the statements that might raise exceptions/errors.
    text = raw_input('Enter something --> ')
# there has to be at least one except clause.
# a single specified errors/exceptions, or a parenthesized list of errors/exceptions
except EOFError:    # ctrl+d
    # handlers for the appropriate errors/exceptions.
    print 'Why did you do an EOF on me?'
# a single specified errors/exceptions, or a parenthesized list of errors/exception
except KeyboardInterrupt:   # ctrl+c
    # handlers for the appropriate errors/exceptions.
    print 'You cancelled the operation'
# if no exception occurs
else:
    print 'You entered {}'.format(text)
