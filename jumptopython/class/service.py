__author__ = '1000938'


# service.py

class Service:
    secret = "two"

    def setname(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" % (a, b, result))


pey = Service()
pey.setname("hong")
print(pey.name)
print(pey.sum(1, 1))
print(Service.sum(pey, 1, 1))