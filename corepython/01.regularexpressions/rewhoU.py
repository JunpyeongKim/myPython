#!/usr/bin/env python
# encoding=utf-8

# rewhoU.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.4 Some Regex Examples
#   - Example 1-3. Universal Version of rewho.py Script
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch01/rewhoU.py
#       - only available on POSIX systems
#       - to maintain two versions of the same script for both Python 2 and 3.

# SyntaxError: from __future__ imports must occur at the beginning of the file
from __future__ import with_statement
import os
from distutils.log import warn as printf
# from __future__ import with_statement
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        printf(re.split('\s\s+|\t', eachLine.rstrip()))
