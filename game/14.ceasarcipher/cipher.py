# cipher.py
# 14. Caesar Cipher
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/chapter14.html
#   - http://inventwithpython.com/cipher.py


# Caesar Cipher

MAX_KEY_SIZE = 26


def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute force a message?')
        # mode = input().lower()  # v3.x
        mode = raw_input().lower()  # v2.x
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')


def getMessage():
    print('Enter your message:')
    # return input()
    return raw_input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        # key = int(input())  # v3.x
        key = int(raw_input())  # v2.x
        if (key >= 1 and key <= MAX_KEY_SIZE):
        # if 1 <= key <= MAX_KEY_SIZE:
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd' or mode[0] == 'b':
        key = -key

    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol

    return translated


mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()

# in brute force mode
# - Doubts may not be pleasant, but certainty is absurd.
# - if key is 8, Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        # print(key, getTranslatedMessage(mode, message, key))  # v3.x
        print key, getTranslatedMessage(mode, message, key)  # v2.x
