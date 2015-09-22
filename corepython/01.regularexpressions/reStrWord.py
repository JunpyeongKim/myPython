#!/usr/bin/env python
# encoding=utf-8

# reStrWord.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.10 Matching from the Beginning and End of Strings and on Word Boundaries

import re


# ^ : start of string
patt = '^The'
target = 'The end.'
m = re.search(patt, target)
print "'" + target + "'.search('", patt, "'):", m
if m is not None:
    print '...group():', m.group()

target = 'end. The'
m = re.search(patt, target)
print "'" + target + "'.search('", patt, "'):", m
if m is not None:
    print '...group():', m.group()

# \b : any word boundary
patt = r'\bthe'
target = 'bite the dog'
m = re.search(patt, target)
print "'" + target + "'.search('", patt, "'):", m
if m is not None:
    print '...group():', m.group()

target = 'bitethe dog'
m = re.search(patt, target)
print "'" + target + "'.search('", patt, "'):", m
if m is not None:
    print '...group():', m.group()

patt = r'\Bthe'
m = re.search(patt, target)
print "'" + target + "'.search('", patt, "'):", m
if m is not None:
    print '...group():', m.group()
