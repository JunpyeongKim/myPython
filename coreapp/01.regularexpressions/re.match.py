#!/usr/bin/env python
# encoding=utf-8

# re.match.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.4 Matching Strings with match()
#
# match(pattern, string, flags=0)
# - match pattern to string
# - match object on success, None on failure


import re

m = re.match('foo', 'foo')  # pattern matches string
print 'm:', m
if m is not None:   # show match if successful
    print '...group():', m.group()

m = re.match('foo', 'bar')  # pattern does not match string
print 'm:', m
if m is not None:
    print '...group():', m.group()

m = re.match('foo', 'foo on the table')  # match succeeds
print 'm:', m
print '...group():', m.group()

print 'group():', re.match('foo', 'foo on  the table').group()

# AttributeError: 'NoneType' object has no attribute 'group'
print 'group():', re.match('foo', 'bar on  the table').group()
