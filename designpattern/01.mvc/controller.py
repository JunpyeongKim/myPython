#!/usr/bin/env python
# encoding=utf-8

# controller.py

# Learning Python Design Patterns, Gennadiy Zlobin
# - http://www.acornpub.co.kr/book/python-design-patterns
#
# 1. Model-View-Controller
# - $ python controller.py
# - Go to http://127.0.0.1:5000 on Browser


import models

app = Flask(__name__, template_folder='views')

@app.route("/")
def index():
    pass

@app.route("/shorten")
def shorten():
    pass

@app.route('/<path:path>')
def redirect_to_full(path=''):
    pass

if __name__ == "__main__":
    app.run(debug=True)
