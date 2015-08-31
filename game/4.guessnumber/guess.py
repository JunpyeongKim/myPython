# guess.py
# 4. Guess The Number
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/inventwithpython_3rd.pdf
#   - http://inventwithpython.com/chapter4.html
#       - http://inventwithpython.com/guess.py


# This is a guess the number game.

import random

guessesTaken = 0

print('Hello! What is your name?')
myName = raw_input()    # 2.x --> input() for 3.x

# 1 <= ~ <= 20
number = random.randint(1, 20)
print('number is ' + str(number))
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')  # There are four spaces in front of print.
    guess = raw_input()
    # try
    # - int('hello'), int('forty-two') --> ValueError
    # - int(' 42 ') --> 42
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')  # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
