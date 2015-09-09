# encoding=utf-8

# truefalsefizz.py

# 10. Tic Tac Toe
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/chapter10.html
#   - http://inventwithpython.com/truefalsefizz.py
#   - http://inventwithpython.com/downloads/


def TrueFizz(message):
    print(message)
    return True


def FalseFizz(message):
    print(message)
    return False


if FalseFizz('Cats') or TrueFizz('Dogs'):
    print('Step1')

if TrueFizz('Hello') or TrueFizz('Goodbye'):
    print('Step2')

if TrueFizz('Spam') and TrueFizz('Cheese'):
    print('Step3')

if FalseFizz('Red') and TrueFizz('Blue'):
    print('Step4')
