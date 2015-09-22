#!/usr/bin/env python
# encoding=utf-8

# reSplit.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.13 Splitting (on Delimiting Pattern) with split()


import re

print re.split(':', 'str1:str2:str3')
print '\n------------------------------'

DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)

# ', ' : split on comma-space
# '(?= (?:\d{5}|[A-Z]{2})) ' : ???
for datum in DATA:
    print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum)

