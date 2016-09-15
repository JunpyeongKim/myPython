#!/usr/bin/env python
# encoding=utf-8

# retasklist.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.4 Some Regex Examples
#   - Example 1-4. Processing the DOS tasklist Command Output
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch01/retasklist.py
#       - can be achieved on Windows-based computers

import os
import re

f = os.popen('tasklist /nh', 'r')
for eachLine in f:
    print re.findall(
        '([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',
        eachLine.rstrip())
f.close()
