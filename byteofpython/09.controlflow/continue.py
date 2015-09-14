# encoding=utf-8

# continue.py

# 9.5. The continue Statement
# - http://www.swaroopch.com/notes/python/#the_continue_statement

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'Too small'
        # skip the rest of the statements in the current loop block and
        # continue to the next iteration of the loop.
        continue
    print 'Input is of sufficient length'
    # Do other kinds of processing here...
