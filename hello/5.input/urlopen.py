# encoding=utf-8

# urlopen.py


import urllib

file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read()
print message
