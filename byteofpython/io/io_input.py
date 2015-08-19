__author__ = 'Junpyeong Kim'


# io_input.py
# 15.1. Input and Output
# - http://www.swaroopch.com/notes/python/#_input_from_user


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


# "sir", "madam", "racecar", "Rise to vote, sir."
'''
    Enter text: sir
    No, it is not a palindrome

    Enter text: madam
    Yes, it is a palindrome

    Enter text: racecar
    Yes, it is a palindrome

    Enter text: Rise to vote, sir.
    Yes, it is a palindrome
'''

something = raw_input("Enter text: ")
if is_palindrome(something):
    print "Yes, it is a palindrome"
else:
    print "No, it is not a palindrome"
