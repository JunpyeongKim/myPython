__author__ = 'Junpyeong Kim'


# oop_methods.py
# 14.3. Methods
# - http://www.swaroopch.com/notes/python/#methods


class Person:
    def say_hi(self):
        print('Hello, how are you?')


p = Person()
p.say_hi()
# The previous 2 lines can also bre written as
# Person().say_hi()