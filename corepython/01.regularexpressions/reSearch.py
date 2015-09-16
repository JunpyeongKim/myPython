#!/usr/bin/env python
# encoding=utf-8

# reSearch.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.5 Looking for a Pattern within a String with search() (Searching versus Matching)
#
# search(pattern, string, flags=0)
# - search for the first occurrence of the pattern anywhere within string
# - match object on success, None on failure
#
# group(num=0)
# - show the successful match, i.e. entire match (or specific subgroup num)


import re

m = re.match('foo', 'seafood')
if m is not None:
    print 'match().group():', m.group()


m = re.search('foo', 'seafood')
if m is not None:
    print 'search().group():', m.group()