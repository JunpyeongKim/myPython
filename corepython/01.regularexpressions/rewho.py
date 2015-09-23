#!/usr/bin/env python
# encoding=utf-8

# rewho.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.4 Some Regex Examples
#   - Example 1-1. Split Output of the POSIX who Command
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch01/rewho.py
#       - only available on POSIX systems

import os
import re

# the output of the who command, presumably saved into a file called whodata.txt
f = open('whodata.txt', 'r')
for eachLine in f:
    print re.split(r'\s\s+', eachLine)

# \t, \n
# str.rstrip() : get rid of the trailing \ns
f = os.popen('who', 'r')
print f
for eachLine in f:
    print re.split('\s\s+|\t', eachLine.rstrip())
f.close()
