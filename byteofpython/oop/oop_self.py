__author__ = 'Junpyeong Kim'


# oop_self.py
# 14.1. The self
# - http://www.swaroopch.com/notes/python/#self


class MyClass:
    # self
    # - Class methods have only one specific difference from ordinary functions.
    # - refers to the object itself.
    # - Python will provide it.
    # - any name fot this parameter -> strongly recommended, "self"
    def method(self, arg1, arg2):
        print "arg1:", arg1, "arg2:", arg2

arg1 = "Argument 1"
arg2 = "Argument 2"

myobject = MyClass()

myobject.method(arg1, arg2)
# automatically converted by Python such as the following.
MyClass.method(myobject, arg1, arg2)
