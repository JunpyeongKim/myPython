#!/usr/bin/env python
# encoding=utf-8

# reRepSpeclGrp.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.9 Repetition, Special Characters, and Grouping


import re

# \w : any alphanumeric character, same as [A-Za-z0-9_]
# + : 1 or more occurrences of preceding regex
# ? : 0 or 1 occurrence(s) of preceding regex
patt = '\w+@(\w+\.)?\w+\.com'

m = re.match(patt, 'nobody@xxx.com')
print "'nobody@xxx.com'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()

m = re.match(patt, 'nobody@www.xxx.com')
print "'nobody@www.xxx.com'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()


# * : 0 or more occurrences of preceding regex
patt = '\w+@(\w+\.)*\w+\.com'

m = re.match(patt, 'nobody@www.xxx.yyy.zzz.com')
print "'nobody@www.xxx.yyy.zzz.com'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()

# sub-group match
patt = '\w\w\w-\d\d\d'
m = re.match(patt, 'abc-123')
print "'abc-123'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()

m = re.match(patt, 'abc-xyz')
print "'abc-xyz'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()

patt = '(\w\w\w)-(\d\d\d)'
m = re.match(patt, 'abc-123')
print "'abc-123'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()
    print '...group(1):', m.group(1)
    print '...group(2):', m.group(2)
    print '...groups():', m.groups()

patt = 'ab'
m = re.match(patt, 'ab')
print "'ab'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()
    print '...groups():', m.groups()

patt = '(ab)'
m = re.match(patt, 'ab')
print "'ab'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()  # entire match
    print '...group(1):', m.group(1)  # subgroup 1
    print '...groups():', m.groups()  # all subgroups

patt = '(a)(b)'
m = re.match(patt, 'ab')
print "'ab'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()  # entire match
    print '...group(1):', m.group(1)  # subgroup 1
    print '...group(2):', m.group(2)  # subgroup 2
    print '...groups():', m.groups()  # all subgroups

patt = '(a(b))'  # two subgroups
m = re.match(patt, 'ab')
print "'ab'.match(", patt, "):", m
if m is not None:
    print '...group():', m.group()  # entire match
    print '...group(1):', m.group(1)  # subgroup 1
    print '...group(2):', m.group(2)  # subgroup 2
    print '...groups():', m.groups()  # all subgroups
