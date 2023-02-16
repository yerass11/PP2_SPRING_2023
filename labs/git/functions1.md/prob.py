class Person():
    def __init__(self, name, nationallity):
        self.name = name
        self.nationallity = nationallity
    def printInfo(self):
        print('Name:', self.name)
        print('Nationallity:', self.nationallity)
    def setSurname(self, surname):
        self.surname = surname
    def getSurname(self):
        return self.surname
    
    
        
    
     

    
class Student(Person):
    def __init__(self, name, nationallity, id, n):
        super().__init__(name, nationallity)
        self.id = id
        self.n = n
        
    def printInfo(self):
        super().printInfo()
        print('Id:', self.id)
        print('n:', self.n)
    
    def triangle(self):
        n = int(input())
        for i in range(n):
            for j in range(2 * n):
                if j >= n - i and j <= n + i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    
        
class Teacher(Person):
    def __init__(self, name, nationality, id):
        super().__init__(name, nationality)
        self.id = id
        
    def printInfo(self):
        super().printInfo()
        print("Id:", self.id)
        
        
#stud = Student("Doka", "Kazakh", "22B030456")
#print(stud.printInfo())
    
t1 = Student({})
print(t1.triangle(5))
   


    
    

    