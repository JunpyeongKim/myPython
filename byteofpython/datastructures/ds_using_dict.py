# ds_using_dict.py
# 12.4. Dictionary
# - http://www.swaroopch.com/notes/python/#dictionary
#   - key : only immutable, simple objects
#   - value : either immutable or mutable objects
#   - not ordered
#   - help(dict)

# 'ab' is short fot 'a'ddress 'b'ook
ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wal.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

# using the indexing operator
print "Swaroop's address is", ab['Swaroop']

# Deleting a key-value pair
del ab['Spammer']

print '\nThere are {} contacts in the address-book\n'.format(len(ab))

# returns a list of tuples
for name, address in ab.items():
    print 'Contact {} at {}'.format(name, address)

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print "\nGuido's address is", ab['Guido']