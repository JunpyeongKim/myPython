# break.py
# 9.4. The break Statement
# - http://www.swaroopch.com/notes/python/#the_break_statement

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        # break out of the loop statement.
        # - any corresponding loop else block is not executed.
        break
    print 'Length of the string is', len(s)
print 'Done'
