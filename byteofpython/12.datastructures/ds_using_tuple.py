# encoding=utf-8

# ds_using_tuple.py

# 12.3. Tuple
# - http://www.swaroopch.com/notes/python/#tuple
#   - immutable
#   - an empty tuple : ()
#   - a tuple with a single item : (2, )

# I would recommend always using parentheses
# to indicate start and end of tuple
# event though parentheses are optional.
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')
# len() indicates that a tuple is a sequence as well.
print 'Number of animals in the zoo is', len(zoo)

# does not lose its identity
# a list within a list, a tuple within a list, a tuple within a tuple, a list within a tuple
new_zoo = 'monkey', 'camel', zoo
print 'Number of cages in the new zoo is ', len(new_zoo)
print 'All animals in new zoo are', new_zoo
# using the indexing operator
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]
print 'Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2])
