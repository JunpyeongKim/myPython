__author__ = 'Junpyeong Kim'


# exceptions_finally.py
# 16.5. Try ... Finally
# - http://www.swaroopch.com/notes/python/#_try_finally

import sys
import time

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = None
try:
    f = open("poem.txt")
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
        sys.stdout.flush()
        print "Press ctrl+c now"
        # To make sure it runs for a while
        time.sleep(2)
except IOError:
    print 'Could not find file poem.txt'
except KeyboardInterrupt:
    print '!! You cancelled the reading from the file.'
finally:
    if f:
        f.close()
    print '(Cleaning up: Closed the file)'
