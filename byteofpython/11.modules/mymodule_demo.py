# encoding=utf-8

# mymodule_demo.py

# 11.4. Making Your Own Modules
# - http://www.swaroopch.com/notes/python/#_making_your_own_modules


# always recommended to prefer the import statement.
# - should be placed either in the same directory or in sys.path
import mymodule

# dotted notation to access members of the module.
mymodule.say_hi()
print 'Version', mymodule.__version__
