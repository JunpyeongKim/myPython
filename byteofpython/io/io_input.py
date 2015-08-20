__author__ = 'Junpyeong Kim'


# io_input.py
# 15.1. Input and Output
# - http://www.swaroopch.com/notes/python/#_input_from_user


def reverse(text):
    # slices from sequences (http://www.swaroopch.com/notes/python/#sequence)
    return text[::-1]


# palindrom in wiki (http://en.wiktionary.org/wiki/palindrome)
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

    Enter text: Rise to vote, sir. (TBD)
    Yes, it is a palindrome
    - Use a tuple (you can find a list of all punctuation marks here) to hold all the forbidden characters,
    - then use the membership test to determine whether a character should be removed or not,
    - i.e. forbidden = (!, ?, ., …​).
'''

something = raw_input("Enter text: ")
if is_palindrome(something):
    print "Yes, it is a palindrome"
else:
    print "No, it is not a palindrome"
