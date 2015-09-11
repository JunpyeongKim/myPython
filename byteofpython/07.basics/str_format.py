# encoding=utf-8

# str_format.py

# 7.4.5. The format method
# - http://www.swaroopch.com/notes/python/#_the_format_method

age = 20
name = 'Swaroop'

print '{0} was {1} years old when he wrote this book'.format(name, age)
print 'Why is {0} playing with that python?'.format(name)
print ''

# numbers are optional
print '{} was {} years old when he wrote this book'.format(name, age)
print 'Why is {} playing with that python?'.format(name)
print ''

# decimal (.) precision of 3 for float '0.333'
print '{0:.3f}'.format(1.0/3)
print '{0:_^11}'.format('hello')
print '{name} wrote {book}'.format(name='Swaroop',
                                   book='A Byte of Python')
print ''

print "a",
print "b",
