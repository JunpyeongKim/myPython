#!/usr/bin/env python
# encoding=utf-8

# reFindalliter.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.11 Finding Every Occurrence with findall() and finditer()

import re


patt = 'car'

s = 'car'
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m

s = 'scary'
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m

s = 'carry the barcardi to the car'
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m

print ''


# re.I : IGNORECASE
patt = r'(th[ia]s)'  # 1 subgroup, 1 match
s = 'This and that.1'
m = re.findall(patt, s, re.I)
print "'" + s + "'.findall('", patt, "'):", m

patt = r'(th[ia])'  # 1 subgroup, 2 matches
s = 'This and that.1'
m = re.findall(patt, s, re.I)
print "'" + s + "'.findall('", patt, "'):", m

# . : any character
patt = r'(th[ia]).+(th[ia])'  # 2 subgroups, 2 matches
s = 'This and that.1'
m = re.findall(patt, s, re.I)
print "'" + s + "'.findall('", patt, "'):", m

patt = r'((th[ia]\w+))'  # 2 subgroups, 2 matches
s = 'This and that.1'
m = re.findall(patt, s, re.I)
print "'" + s + "'.findall('", patt, "'):", m

print ''


#
patt = r'(th\w+) and (th\w+)'
s = 'This and that.'
m = re.finditer(patt, s, re.I)
print "'" + s + "'.finditer('", patt, "'):", m
if m is not None:
    n = m.next()
    print '...next()', n
    print '...next().group()', n.group()
    print '...next().group(1)', n.group(1)
    print '...next().group(2)', n.group(2)
    print '...next().groups()', n.groups()

# Python 3
# print 'Python 3:', next(re.finditer(patt, s, re.I)).groups()

print 'List Comprehension:', [g.groups() for g in re.finditer(patt, s, re.I)]

print ''

#
patt = r'(th\w+)'
s = 'This and that.'
m = re.findall(patt, s, re.I)
print "'" + s + "'.findall('", patt, "'):", m

it = re.finditer(patt, s, re.I)
print "'" + s + "'.finditer('", patt, "'):", it
if it is not None:
    g = it.next()
    print '...next()', g
    print '...next().groups()', g.groups()
    print '...next().group(1)', g.group(1)
    g = it.next()
    print '...next()', g
    print '...next().groups()', g.groups()
    print '...next().group(1)', g.group(1)



