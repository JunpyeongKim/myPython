# encoding=utf-8

# if.py

# 9.1. The if statement
# - http://www.swaroopch.com/notes/python/#_the_if_statement
#   - no switch statement in Python
#       - use a dictionary

number = 23
guess = int(raw_input('Enter an integer : '))
    # raw_int() returns a string.
    # the int is a class.

# a colon followed by their corresponding block of statements.
if guess == number:
    # New block starts here
    print 'Congratulations, you guessed it.'
    print '(but you do not win any prizes!)'
    # New block ends here
elif guess < number:
    # Another block
    print 'No, it is a little higher than that'
    # You can do whatever you want in a block...
else:
    print 'No, it is a little lower than that'
    # you must have guessed > number to reach here

print 'Done'
# This last statement is always executed,
# after the if statement is executed.

# no switch statement in Python
# - use a dictionary.
