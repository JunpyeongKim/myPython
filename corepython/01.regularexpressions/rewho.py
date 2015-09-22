#!/usr/bin/env python
# encoding=utf-8

# rewho.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.4 Some Regex Examples
#   - Example 1-1. Split Output of the POSIX who Command
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch01/rewho.py

import os
import re

f = os.popen('who', 'r')
for eachLine in f:
    print re.split('\s\s+|\t', eachLine.rstrip())
f.close()
