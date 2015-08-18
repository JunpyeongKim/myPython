__author__ = 'Junpyeong Kim'


# oop_objvar.py
# 14.5. Class And Object Variables
# - http://www.swaroopch.com/notes/python/#class_obj_vars


class Robot:
    # docstrings for class using triple double-quoted strings
    # - Robot.__doc__
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    # A private variable, using the double underscore prefix.
    # - All class members are public.
    # - Robot.__privatevar --> "AttributeError"
    __privateclassvar = "private-class-var"

    def __init__(self, name):
        # docstrings for method using triple double-quoted strings
        # - Robot.__init__.__doc__
        """Initializes the data."""

        # A object variable
        self.name = name

        # A private variable.
        self.__privateobjvar = "private-obj-var"

        print "(Initializing {})".format(self.name)
        print "(Initializing {})".format(self.__privateobjvar)

        # When this robot is created, the robot
        # adds to the population
        # the same as "self.__class__.population += 1"
        Robot.population += 1

    def die(self):
        # docstrings for method using triple double-quoted strings
        # - Robot.die.__doc__
        """I am dying."""
        print "{} is being destroyed!".format(self.name)

        Robot.population -= 1

        if Robot.population == 0:
            print "{} was the last one.".format(self.name)
        else:
            print "There are still {:d} robots working".format(Robot.population)

    def say_hi(self):
        # docstrings for method using triple double-quoted strings
        # - Robot.say_hi.__doc__
        """Greeting by the robot.

        Yeah, they can do that."""
        print "Greetings, my masters call me {}.".format(self.name)
        print "Greetings, my masters call me {}.".format(self.__privateclassvar)
        print "Greetings, my masters call me {}.".format(self.__privateobjvar)

    # Decorator : @classmethod or @staticmethod(?)
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print "We have {:d} robots.".format(cls.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do some work here.\n"

# print
# print "access a private object variables"
# print "droid1.__privateobjvar:", droid1.__privateobjvar
# print "droid2.__privateobjvar:", droid2.__privateobjvar

print "Robots have finished their work. So let's destroy them."

droid1.die()
droid2.die()

Robot.how_many()

# print
# print "---docstrings---"
#
# print "Robot.__doc__:", Robot.__doc__
# print "Robot.__init__.__doc__:", Robot.__init__.__doc__
# print "Robot.die.__doc__:", Robot.die.__doc__
# print "Robot.say_hi.__doc__:", Robot.say_hi.__doc__
# print "Robot.how_many.__doc__:", Robot.how_many.__doc__

# print
# print "access a private class variable "
# print "Robot.__privateclassvar: ", Robot.__privateclassvar
