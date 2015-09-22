#!/usr/bin/env python
# encoding=utf-8

# reCharClass.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.8 Creating Character Classes ([])


import re


m = re.match('[cr][23][dp][o2]', 'c3po')  # matches 'c3po;
print "'c3po'.match([]):", m
if m is not None:
    print '...group():', m.group()


m = re.match('[cr][23][dp][o2]', 'c2do')  # matches 'c2do'
print "'c2do'.match([]):", m
if m is not None:
    print '...group():', m.group()


print ''
m = re.match('r2d2|c3po', 'c2do')  # does not match 'c2do'
print "'c2do'.match(|):", m
if m is not None:
    print '...group():', m.group()


m = re.match('r2d2|c3po', 'r2d2')  # matches 'r2d2'
print "'r2d2'.match(|):", m
if m is not None:
    print '...group():', m.group()
