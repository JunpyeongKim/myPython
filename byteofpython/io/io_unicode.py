__author__ = 'Junpyeong Kim'


# encoding=utf-8
# Whenever we write a program that uses Unicode literals,
# we have to put # encoding=utf-8 comment at the top of our porgram.


# io_unicode.py
# 15.4. Unicode
# - http://www.swaroopch.com/notes/python/#unicode


import io


# However, when to a file or on the Internet,
# we need to convert our unicode strings into a format called "UTF-8"
f = io.open("abc.txt", "wt", encoding="utf-8")
# if other non-English languages, use the unicode type
# i.e. type(u"hello world") -> <type 'unicode'>
f.write(u"Image non-English language here")
f.close()

# However, when to a file or on the Internet,
# we need to convert our unicode strings into a format called "UTF-8"
text = io.open("abc.txt", encoding="utf-8").read()
print text
