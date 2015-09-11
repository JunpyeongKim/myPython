# encoding=utf-8

# oop_subclass.py

# 14.6. Inheritance
# - http://www.swaroopch.com/notes/python/#_inheritance


class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        '''Tell my details.'''
        print 'Name: "{}" Age: "{}"'.format(self.name, self.age),   # not print a \n


# the reuse of code through the inheritance mechanism.
# Specify the base class names in a tuple. --> "multiple inheritance"
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        # Explicitly call the constructor.
        # - Python does not automatically call the constructor of the base class.
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)


# the reuse of code through the inheritance mechanism.
# Specify the base class names in a tuple. --> "multiple inheritance"
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        # Explicitly call the constructor.
        # - Python does not automatically call the constructor of the base class.
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.marks)

t = Teacher('Mrs. Shrividya', 40, 3000)
s = Student('Swaroop', 25, 75)


# prints a blank line
print

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    # Python always starts looking for methods in the actual type.
    # If it could not find the method, it starts looking at the methods belonging to its base classes
    # one bye one in the order they are specified in the tuple in the class definition.
    # --> "Polymorphism"
    #       - you can refer to a teacher or student object as a SchoolMember object.
    #       - the object can be treated as an instance of the parent class.
    member.tell()
