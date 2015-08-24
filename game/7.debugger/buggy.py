# buggy.py
# 7.7 Find the Debugger
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
# - http://inventwithpython.com/buggy.py

import random


number1 = random.randint(1, 10)
number2 = random.randint(1, 10)

print('What is ' + str(number1) + ' + ' + str(number2) + '?')

# semantic error
answer = raw_input('> ')
if answer == number1 + number2:
# if int(answer) == number1 + number2:
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))


# No semantic error
# answer = input('> ')
# if answer == number1 + number2:
#     print('Correct')
# else:
#     print('Nope! The answer is ' + str(number1 + number2))
