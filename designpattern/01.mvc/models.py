#!/usr/bin/env python
# encoding=utf-8

# models.py

# Learning Python Design Patterns, Gennadiy Zlobin
# - http://www.acornpub.co.kr/book/python-design-patterns
#
# 1. Model-View-Controller
# - $ python controller.py
# - Go to http://127.0.0.1:5000 on Browser


import pickle


class Url(object):
    @classmethod
    def shorten(cls, full_url):
        pass

    @classmethod
    def get_by_short_url(cls, short_url):
        pass

    def __create_short_url(self):
        pass

    def __increment_string(self, string):
        pass

    @staticmethod
    def __load_last_short_url():
        pass

    @staticmethod
    def __save_last_short_url():
        pass

    @staticmethod
    def __load_url_mapping():
        pass

    @staticmethod
    def __save_url_mapping(instance):
        pass
