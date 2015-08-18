__author__ = 'Junpyeong Kim'


# oop_subclass.py
# 14.6.Inheritance
# - http://www.swaroopch.com/notes/python/#_inheritance


class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        '''Tell my details.'''
        print 'Name: "{}" Age: "{}"'.format(self.name, self.age),


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "{:d}"'.format(self.marks)

t = Teacher('Mrs. Shrividya', 40, 3000)
s = Student('Swaroop', 25, 75)

# prints docstrings
# print("SchoolMember Docstrings:", SchoolMember.doc)
# print ""

# prints a blank line
print

members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
