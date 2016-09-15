#!/usr/bin/env python
# encoding=utf-8

# reSubn.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.12 Searching and Replacing with sub() and subn()
#   - find and replace functionality

import re

#
m = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
print m

m = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
print m

print ''

#
print re.sub('[ae]', 'X', 'abcdef')
print re.subn('[ae]', 'X', 'abcdef')

print ''

# {N} : N occurrences of preceding regex
# {M,N} : M to N occurrences of preceding regex
# \N : saved subgroup N
print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991')