# encoding=utf-8

# buggy.py

# 7.7 Find the Debugger
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/chapter7.html
#       - Syntax error
#       - Runtime error (=Crash)
#       - Semantic error
#   - http://inventwithpython.com/buggy.py
#   - http://inventwithpython.com/downloads/

# Topics Covered In This Chapter:
# ·        3 Different Types of Errors
# ·        IDLE’s Debugger
# ·        Stepping Into, Over, and Out
# ·        Go and Quit
# ·        Break Points


import random


number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print('What is ' + str(number1) + ' + ' + str(number2) + '?')

# answer = input('> ')  # v3.x
answer = raw_input('> ')  # v2.x
if answer == number1 + number2:  # semantic error
# if int(answer) == number1 + number2:  # no semantic error
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))


# No semantic error in v2.x
# answer = input('> ')
# if answer == number1 + number2:
#     print('Correct')
# else:
#     print('Nope! The answer is ' + str(number1 + number2))
