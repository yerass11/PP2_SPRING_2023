class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#using the person class to create an object

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Alua", "Omar")
x.printname()