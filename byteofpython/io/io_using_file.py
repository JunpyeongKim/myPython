__author__ = 'Junpyeong Kim'


# io_using_file.py
# 15.2. Files
# - http://www.swaroopch.com/notes/python/#_files
#   - by creating an object of the file class
#   - The ability depends on the mode for the file opening


poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# Open for 'w'riting
# - the mode
#   - read mode('r'), write mod('w'), append mode('a'),
#   - text mode('t'), binary mode('b')
# - $ help(open)
# - By default, 'rt' mode, i.e. 'read text file' is the default mode.
#   - open() considers the file to be a 't'ext file and opens it in 'r'ead mode.
f = open('poem.txt', 'w')

# Write text to file
f.write(poem)

# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break

    # The 'line' already has a newline
    # at the end of each line
    # since it is reading from a file.
    print line,

# close the file
f.close()