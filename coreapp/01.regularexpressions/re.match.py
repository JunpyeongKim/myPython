#!/usr/bin/env python
# encoding=utf-8

# re.match.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.4 Matching Strings with match()
#
# match(pattern, string, flags=0)
# - match the pattern to the string, starting at the beginning.
# - match object on success, None on failure
#
# group(num=0)
# - show the successful match, i.e. entire match (or specific subgroup num)


import re

#
m = re.match('foo', 'foo')  # pattern matches string
print 'm:', m
if m is not None:   # show match if successful
    print '...group() 1:', m.group()


#
m = re.match('foo', 'bar')  # pattern does not match string
print 'm:', m
if m is not None:
    print '...group() 2:', m.group()


#
m = re.match('foo', 'foo on the table')  # match succeeds
print 'm:', m
print '...group() 3:', m.group()


#
print 'group() 1:', re.match('foo', 'foo on  the table').group()


#
print 'group() 2:', re.match('foo', 'foobar on  the table').group()


#
print 'group() 3:', re.match('foo', 'foo foobar on  the table').group()

# AttributeError: 'NoneType' object has no attribute 'group'
try:
    print 'group() 4:', re.match('foo', 'bar is not in the middle of foo on the table').group()
except AttributeError, e:
    print 'AttributeError:', e


try:
    print 'group() 5:', re.match('foo', 'table under the foo').group()
except AttributeError, e:
    print 'AttributeError:', e

try:
    print 'group() 6:', re.match('foo', 'bar on the table').group()
except AttributeError, e:
    print 'AttributeError:', e
