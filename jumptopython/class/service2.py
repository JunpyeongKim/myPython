__author__ = 'Junpyeong Kim'


# service.py

class Service:
    secret = "two"

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" % (a, b, result))


pey = Service("hong")
print(pey.name)
print(pey.sum(1, 1))
print(Service.sum(pey, 1, 1))