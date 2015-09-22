#!/usr/bin/env python
# encoding=utf-8

# reMatch.py

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


m = re.match('foo', 'foo')  # pattern matches string
print "'foo'.match():", m
if m is not None:  # show match if successful
    print '...group():', m.group()


m = re.match('foo', 'bar')  # pattern does not match string
print "'bar'.match():", m
if m is not None:
    print '...group():', m.group()


print ''
m = re.match('foo', 'foo on the table')  # match succeeds
print "'foo on the table'.match():", m
if m is not None:
    print '...group():', m.group()


print "'foo on  the table'.match().group():", re.match('foo', 'foo on  the table').group()


print "'foobar on  the table'.match().group():", re.match('foo', 'foobar on  the table').group()


print "'foo foobar on  the table'.match().group():", re.match('foo', 'foo foobar on  the table').group()


# AttributeError: 'NoneType' object has no attribute 'group'
print ''
try:
    print "'bar is not in the middle of foo on the table'.match().group():", \
        re.match('foo', 'bar is not in the middle of foo on the table').group()
except AttributeError, e:
    print '\n\tAttributeError:', e


try:
    print "'table under the foo:", \
        re.match('foo', 'table under the foo').group()
except AttributeError, e:
    print '\n\tAttributeError:', e

try:
    print "'bar on the table:", \
        re.match('foo', 'bar on the table').group()
except AttributeError, e:
    print '\n\tAttributeError:', e
