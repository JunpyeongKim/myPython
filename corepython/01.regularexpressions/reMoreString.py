#!/usr/bin/env python
# encoding=utf-8

# reMoreString.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.6 Matching More than One String (|)


import re

bt = 'bat|bet|bit'  # regex pattern: bat, bet, bit
m = re.match(bt, 'bat')  # 'bat' is a match
print "'bat'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.match(bt, 'blt')  # no match for 'blt'
print "'blt'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.match(bt, 'He bit me!')  # does not match string
print "'He bit me!'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.search(bt, 'He bit me!')  # found 'bit' via search
print "'He bit me!'.search():", m
if m is not None:
    print '...group():', m.group()
