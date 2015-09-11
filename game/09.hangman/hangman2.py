# encoding=utf-8

# hangman2.py

# 9. Hangman
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/chapter9.html
#   - http://inventwithpython.com/hangman.py
#   - http://inventwithpython.com/downloads/

# Topics Covered In This Chapter:
# ·        Multi-line Strings
# ·        Methods
# ·        Lists
# ·        The append() and reverse() list methods
# ·        The lower(), upper(), split(), startswith(), and endswith() string methods
# ·        The in and not in operators
# ·        The range() and list() functions
# ·        del statements
# ·        for loops
# ·        elif statements

# spam = [1, 2, 3, 4, 5, 6, 'meow', 'woof']
# spam.reverse() --> ['meow', 'woof', 6, 5, 4, 3, 2, 1]


import random


HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''']


# favorite1 = {'fruit': 'apples', 'number': 42, 'animal': 'cats'}
# favorite2 = {'animal': 'cats', 'number': 42, 'fruit': 'apples'}
# favorite1 == favorite2 --> True

# listFavs1 = ['apples', 'cats', 42]
# listFavs2 = ['cats', 42, 'apples']
# listFavs1 == listFavs2 --> False

# spam = {'0': 'a string', 0: 'an interger'}
# spam[0] vs. spam['0']
# spam.keys() --> dict_keys type --> list(spam.keys())
# spam.values() --> dict_values type --> list(spam.values())
words = {'Colors': 'red orange yellow green blue indigo, violet white black brown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapazoid chevron '
                   'pentagon hexagon septagon octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana '
                   'cantaloupe mango strawberry tomato'.split(),
         'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat '
                    'leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark '
                    'sheep skunk tiger turkey turtle weasel whale wolf wombat zebra'.split()}


def getRandomWord(wordDict):
    # This function returns a random string from the passed list of strings.
    # random.randint(0, 9) == random.choice(list(range(0, 10)))
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    # print()  # v3.x
    print ''  # v2.x

    # print('Missed letters:', end=' ')  # v3.x
    print 'Missed letters:',  # v2.x
    for letter in missedLetters:
        # print(letter, end=' ')  # v3.x
        print letter,  # v2.x
    # print()  # v3.x
    print ''  # v2.x

    blanks = '_' * len(secretWord)

    # (*) loop unrolling
    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        # print(letter, end=' ')  # v3.x
        print letter,  # v2.x

    # print()  # v3.x
    print ''  # v2.x


def getGuess(alreadyGuessed):
    # Returns the letter the player entered.
    # This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        # guess = input()  # v3.x
        guess = raw_input()  # v2.x
        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    # (cf) endswith(someString)
    # return input().lower().startswith('y')  # v3.x
    return raw_input().lower().startswith('y')  # v2.x


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
# a, b, c = ['apples', 'cats', 42] to unpack
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

print '( 3secretWord is', secretWord, 'in', secretKey,')'

while True:
    print('The secret word is in the set ' + secretKey)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            # print('Yes! The secret word is "' + secretWord + '"! You have won!')  # v3.x
            print('Yes! The secret word is "', secretWord + '"! You have won!')  # v2.x
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done.)
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretKey = getRandomWord(words)
            print '(Again) secretWord is', secretWord
        else:
            break
