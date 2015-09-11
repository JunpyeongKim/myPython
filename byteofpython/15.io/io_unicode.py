# encoding=utf-8
    # Whenever we write a program that uses Unicode literals,
    # we have to put # encoding=utf-8 comment at the top of our program.

# io_unicode.py

# 15.4. Unicode
# - http://www.swaroopch.com/notes/python/#unicode


import io


# However, when to a file or on the Internet,
# we need to convert our unicode strings into a format called "UTF-8"
f = io.open("abc.txt", "wt", encoding="utf-8")

# if other non-English languages, use the unicode type
# i.e. type(u"hello world") --> <type 'unicode'>
f.write(u"Image non-English language here")
f.close()

# However, when to a file or on the Internet,
# we need to convert our unicode strings into a format called "UTF-8"
text = io.open("abc.txt", encoding="utf-8").read()
print text

'''
    learn more about unicode,
    1."The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets"
        - http://www.joelonsoftware.com/articles/Unicode.html
    2. Python Unicode Howto
        - http://docs.python.org/2/howto/unicode.html
    3.Pragmatic Unicode talk by Nat Batchelder
        - http://nedbatchelder.com/text/unipain.html
'''
