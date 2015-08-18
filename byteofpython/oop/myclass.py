__author__ = 'Junpyeong Kim'


# myclass.py
# - http://www.swaroopch.com/notes/python/#self


class MyClass:
    def method(self, arg1, arg2):
        print("this is the method of class")

myobject = MyClass()
arg1 = 1
arg2 = 2
myobject.method(arg1, arg2)   # MyClass.method(myobject, arg1, arg2)