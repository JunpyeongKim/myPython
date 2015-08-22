# mymodule_demo2.py
# 11.4. Making Your Own Modules
# - http://www.swaroopch.com/notes/python/#_making_your_own_modules

# always recommended to prefer the import statement.
# - should be placed in the same directory or in sys.path
from mymodule import say_hi, __version__

# should avoid using import-star
# - should be placed in the same directory or in sys.path
# from mymodule import *

say_hi()
# not import version because it starts with double underscores.
print 'Version', __version__
