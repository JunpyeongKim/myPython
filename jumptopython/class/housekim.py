__author__ = '1000938'


# housekim.py

class HousePark:
    lastname = "Park"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s travels in %s" % (self.fullname, where))

    def love(self, other):
        print("%s falled in love with %s" % (self.fullname, other.fullname))

    def __add__(self, other):
        print("%s married %s" % (self.fullname, other.fullname))

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass


class HouseKim(HousePark):
    lastname = "Kim"

pey = HousePark("pey")
print(type(pey))
print(pey.travel("Thai"))

juliet = HouseKim("juliet")
print(type(juliet))
print(juliet.travel("Iceland"))

pey.love(juliet)
pey + juliet