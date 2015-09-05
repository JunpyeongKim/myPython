# encoding=utf-8

# gui.py


import easygui

user_response = easygui.msgbox("Hello There!")
print user_response

flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                           choices = ['Vanila', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + flavor)

flavor = easygui.choicebox("What is your favorite ice cream flavor?",
                           choices = ['Vanila', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + str(flavor))

flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                          default = 'Vanila')
easygui.msgbox("You picked " + str(flavor))

flavor = easygui.integerbox("What's your guess, matey?")
easygui.msgbox("You picked " + str(flavor))
