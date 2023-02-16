class Person:
    """описание человека"""
    def __init__(self, name, nationality):
        """constructor"""
        self.name = name
        self.nationality = nationality


    def printInfo(self):
        """print """
        print(self.name, self.nationality)
    
    def setSurname(self, surname):
        """set a surname"""
        self.surname = surname
    
    def getSurname(self):
        """print a surname"""
        print(self.surname)



class Student(Person):
    """описание студента"""
    def __init__(self, name, nationality, id, n):
        """give id"""
        super().__init__(name, nationality)
        self.id = id
        self.n = n

    def printInfo(self):
        """print info"""
        print(self.name, self.nationality, self.id)
    
    def rhombus(self):
        k = self.n // 2
        l = r = k
        for i in range(k + 1):
            for j in range(self.n):
                if l < 0:
                    break
                if (l == j or r == j):
                    print("*", end = "")
                else: 
                    print(" ", end = "")
            l -= 1
            r += 1
            print()

        l += 2
        r -= 2

        for i in range(k + 1):
            for j in range(self.n):
                if l > k:
                    break
                if (l == j or r == j):
                    print("*", end = "")
                else: 
                    print(" ", end = "")
            l += 1
            r -= 1
            print()

class Teacher(Person):
    """описание учителя"""
    def __init__(self, name, nationality, t_id):
        """give teacher's id"""
        super().__init__(name, nationality)
        self.t_id = t_id

    def printInfo(self):
        """print Info"""
        print(self.name, self.nationality, self.t_id)

#Person
p1 = Person("Mark", "American")
p1.setSurname("Zuckerberg")
p1.printInfo()
p1.getSurname()

#Student
p1 = Student("Yerass1ll", "Kazakh", "22B030286", 7)
p1.setSurname("Saiman")
p1.printInfo()
p1.getSurname()
p1.rhombus()

#Teacher
p1 = Teacher("Arnur", "Kazakh", "101346")
p1.setSurname("Kelgenbaev")
p1.printInfo()
p1.getSurname()