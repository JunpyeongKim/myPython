#!/usr/bin/env python
# encoding=utf-8

# reExtension.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 1.3.14 Extension Notations (?...)
#   - (?iLmsux)


import re

# re.I : IGNORECASE --> ?i
patt = r'(?i)yes'
s = 'yes? Yes. YES!!'
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m
print ''

patt = r'(?i)th\w+'
s = 'The quickest way is through this tunnel.'
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m
print ''

# re.M : MULTILINE
patt = r'(?im)(^th[\w ]+)'
s = """
This line is the first,
another line,
that line, it's the best
"""
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m
print ''

# re.S : DOTALL --> . includes \n
patt = r'th.+'
s = '''
The first line
the second line
the third line
'''
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m

patt = r'(?s)th.+'
s = '''
The first line
the second line
the third line
'''
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m
print ''

# re.X : VERBOSE
# - suppressing whitespace characters within regexes
# - hash/comment/octothorpe symbols (#) can also be used to start a comment
patt = r'''(?x)
\((\d{3})\) # area code
[ ] # space
(\d{3}) # prefix
- # dash
(\d{4}) # endpoint number
'''
s = '(800) 555-1212'
m = re.search(patt, s)
print "'" + s + "'.search('", patt, "'):", m
print '....groups():', m.groups()
print ''

# (?:) : can group parts of a regex, but it does not save them
#        for future retrieval or use
# * : 0 or more occurrences of preceding regex
patt = r'http://(?:\w+\.)*(\w+\.com)'
s = 'http://google.com http://www.google.com http://code.google.com'
m = re.findall(patt, s)
print "'" + s + "'.findall(\n\t'", patt, "'\n\t):", m
print ''

patt = r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})'
s = '(800) 555-1212'
m = re.search(patt, s)
print "'" + s + "'.search('", patt, "'):", m
print '...groupdict():', m.groupdict()
print ''

patt = r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})'
r = '(\g<areacode>) \g<prefix>-xxx'
s = '(800) 555-1212'
m = re.sub(patt, r, s)
print "'" + s + "'.sub(\n\t'", patt, "', \n\t'", r, "'\n\t):", m


#
patt = r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)'
s = '(800) 555-1212 800-555-1212 18005551212'
m = bool(re.match(patt, s))
print "'" + s + "'\n\t.match('", patt, "')\n\t\t:", m
print ''

patt = r'''(?x)

    # match (800) 555-1212, save areacode, prefix, no.
    \((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})

    # space
    [ ]

    # match 800-555-1212
    (?P=areacode)-(?P=prefix)-(?P=number)

    # space
    [ ]

    # match 18005551212
    1(?P=areacode)(?P=prefix)(?P=number)

'''
s = '(800) 555-1212 800-555-1212 18005551212'
m = bool(re.match(patt, s))
print "'" + s + "'\n\t.match('", patt, "')\n\t\t:", m
print ''

patt = r'\w+(?= van Rossum)'
s = '''
    Guido van Rossum
    Tim Peters
    Alex Martelli
    Just van Rossum
    Raymond Hettinger
'''
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m
print ''

patt = r'(?m)^\s+(?!noreply|postmaster)(\w+)'
s = '''
    sales@phptr.com
    postmaster@phptr.com
    eng@phptr.com
    noreply@phptr.com
    admin@phptr.com
'''
m = re.findall(patt, s)
print "'" + s + "'.findall('", patt, "'):", m
print ''

patt = r'(?m)^\s+(?!noreply|postmaster)(\w+)'
s = '''
 sales@phptr.com
 postmaster@phptr.com
 eng@phptr.com
 noreply@phptr.com
 admin@phptr.com
'''
m = ['%s@aw.com' % e.group(1) for e in re.finditer(patt, s)]
print "List Comprehension - \n'" + s + "'.finditer('", patt, "'):", m
print ''

patt = r'(?:(x)|y)(?(1)y|x)'
s = 'xy'
m = bool(re.search(patt, s))
print "'" + s + "'.search('", patt, "'):", m

patt = r'(?:(x)|y)(?(1)y|x)'
s = 'xx'
m = bool(re.search(patt, s))
print "'" + s + "'.search('", patt, "'):", m