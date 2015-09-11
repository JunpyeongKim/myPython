# encoding-utf8

# setup.py

# Appendix C. Py2exe
# - Invent Your Own Computer Games with Python 3e, IAl Sweigart
#   - http://inventwithpython.com/

# py2exe for Windows
# - http://www.py2exe.org/ --> Download --> py2exe-0.6.9.win64-py2.7.amd64.exe

# How to compile
# C:\workspace> python setup.py py2exe
# - go to dist/ folder


from distutils.core import setup
import py2exe

setup(console=['hello.py'])
