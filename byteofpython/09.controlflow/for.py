# encoding=utf-8

# for.py

# 9.3. The for loop
# - http://www.swaroopch.com/notes/python/#_the_for_loop

# range() generates a sequence of numbers.
# - only one number at a time.
# - the step count, i.e. 2 : range(1, 5, 2)
# - e.g. list(range(1, 5))
for i in range(1, 5):
    print i
# optional
# - is always executed once after the for loop is over unless a break statement is encountered.
else:
    print 'The for loop is over'
