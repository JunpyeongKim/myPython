__author__ = 'Junpyeong Kim'


# oop_init.py
# 14.4.The init method
# - http://www.swaroopch.com/notes/python/#init


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()