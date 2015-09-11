# encoding=utf-8

# ds_set.py

#  12.6. Set
# - http://www.swaroopch.com/notes/python/#set
#   - unordered collections of simple objects.
#   - the existence is more important than the order or how many times it occurs.

bri = set(['brazil', 'russia', 'india'])
print 'bric is', bri

if 'india' in bri:
    print 'india is in bri'
else:
    print 'india is not in bri'

if 'usa' in bri:
    print 'usa is in bri'
else:
    print 'usa is not in bri'

bric = bri.copy()
print '(Copy) birc is', bric

bric.add('china')
print '(Add) bric is', bric

if bric.issuperset(bri):
    print 'bric is superset of bri'
else:
    print 'bric is not superset of bri'

bri.remove('russia')
print '(Remove) bri is', bri

if bri & bric:  # OR bri.intersection(bric)
    print 'Intersection is', bri & bric
# if bri.intersection(bric):
#     print 'Intersection is', bri.intersection(bric)
else:
    print 'not intersected'
