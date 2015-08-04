__author__ = '1000938'

# tabto4.py

import re
import sys


def usage():
    print("Usage: python %s filename" % sys.argv[0])

try: f = open(sys.argv[1])
except: usage(); sys.exit(2)

msg = f.read()
f.close()

# r : raw
p = re.compile(r'\t')
changed = p.sub(" "*4, msg)

f = open(sys.argv[1], 'w')
f.write(changed)
f.close()
