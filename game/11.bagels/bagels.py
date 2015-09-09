# encoding=utf-8

# bagels.py

# 11. Bagels
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/chapter11.html
#   - http://inventwithpython.com/bagels.py
#   - http://inventwithpython.com/downloads/

# Topics Covered In This Chapter:
# ·        Augmented Assignment Operators, +=, -=, *=, /=
# ·        The random.shuffle() Function
# ·        The sort() and join() List Methods
# ·        String Interpolation (also called String Formatting)
# ·        Conversion Specifier %s
# ·        Nested Loops


import random


def getSecretNum(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))  # use list() because range() returns an iterator of a list-like collection.
    random.shuffle(numbers)  # rather modifies the list you pass.
    print '(Shuffled) numbers is ', numbers
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    # Returns a string with the pico, fermi, bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')

    if len(clue) == 0:
        return 'Bagels'

    print '(Before sorting) clue is', clue
    clue.sort()  # in alphabetical or numerical order
    print '(After sorting) clue is', clue

    return ' '.join(clue)


def isOnlyDigits(num):
    # Returns True if num is a string made up only of digits. Otherwise returns False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    # return input().lower().startswith('y')  # v3.x
    return raw_input().lower().startswith('y')  # v2.x


NUMDIGITS = 3
MAXGUESS = 10


# string interpolation or string formatting
# - NUMDIGITS will be automatically converted to a string.
print('I am thinking of a %s-digit number. Try to guess what it is.' %(NUMDIGITS))
print('Here are some clues:')
print('When I say:  That means:')
print(' Pico        One digit is correct but in the wrong position.')
print(' Fermi       One digit is correct and in the right position.')
print(' Bagels      No digit is correct.')

while True:
    secretNum = getSecretNum(NUMDIGITS)
    # string interpolation or string formatting
    # - MAXGUESS will be automatically converted to a string.
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (numGuesses))
            # guess = input()  # v3.x
            guess = raw_input()  # 2.x

        clue = getClues(guess, secretNum)
        # print(clue)  # v3.x
        print '(Clue): ', clue  # v2.x
        numGuesses += 1

        if guess == secretNum:
            break

        if numGuesses > MAXGUESS:
            # string interpolation or string formatting
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    if not playAgain():
        break
