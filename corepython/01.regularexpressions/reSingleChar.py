#!/usr/bin/env python
# encoding=utf-8

# reSingleChar.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.7 Matching Any Single Character (.)
#   - cannot match a \n or a non-character, i.e. the empty string


import re

#
anyend = '.end'
m = re.match(anyend, 'bend')  # dot matches 'b'
print "'bend'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.match(anyend, 'end')  # no char to match
print "'end'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.match(anyend, '\nend')  # any char except \n
print "'\\nend'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.search('.end', 'The end.')  # matches ' ' in search
print "'The end.'.match():", m
if m is not None:
    print '...group():', m.group()


#
print ''

patt314 = '3.14'  # regex dot
pi_patt = '3\.14'  # literal dot (dec. point)

m = re.match(pi_patt, '3.14')  # exact match
print "'3.14'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.match(patt314, '3014')  # dot matches '0'
print "'3014'.match():", m
if m is not None:
    print '...group():', m.group()


m = re.match(patt314, '3.14')  # dot matches '.'
print "'3.14'.match():", m
if m is not None:
    print '...group():', m.group()
