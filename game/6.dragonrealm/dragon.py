# dragon.py
# 6. Dragon Realm
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/inventwithpython_3rd.pdf
#       - http://inventwithpython.com/chapter6.html
#       - http://inventwithpython.com/dragon.py

import random
import time


# if call displayIntro() before its definition, NameError is raised.
# displayIntro()


def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')


def chooseCave():
    # Variables created in a function call can be only
    # be read or modified during that function call.
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = raw_input()  # v2.x --> input() for v3.x

    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print('')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == friendlyCave:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


# Variables defined in the global scope can be read outside or inside functions,
# but can only be modified outside of all functions.
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = raw_input()  # v2.x --> input() for v3.x
