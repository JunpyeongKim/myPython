#!/usr/bin/env python
# encoding=utf-8

# rewho3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.4 Some Regex Examples
#   - Example 1-2. Python 3 Version of rewho.py Script
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch01/rewho3.py
#       - only available on POSIX systems
#       - with, print()
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch01/rewho3-hacker.py
#           - ???

import os
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split('\s\s+|\t', eachLine.rstrip()))
