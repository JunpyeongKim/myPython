# encoding=utf-8

# letters.py


letters = ['a', 'b', 'c', 'd', 'e']

# slicing
print letters[1:4]

print letters[1], type(letters[1])
print letters[1:2], type(letters[1:2])

print letters[:2]
print letters[2:]
print letters[:]

print letters
letters[2] = 'z'
print letters
letters[2] = 'c'

# append
letters.append('n')
print letters

# extend
letters.extend(['p', 'q', 'r'])
print letters

# insert
letters.insert(2, 'z')
print letters

# append vs. extend
letters.extend(['f', 'g', 'h'])
print letters
letters.append(['f', 'g', 'h'])
print letters

# remove
letters.remove('c')
print letters

letters.remove('f')  # ValueError