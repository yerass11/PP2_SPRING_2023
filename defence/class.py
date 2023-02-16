class Animal:
    legs = 4
    tail = 1
    def __init__(self, voice, color):
        self.voice = voice
        self.color = color


    def giveVoice(self):
        print(self.legs, self.tail, self.voice, self.color)
    
    def setnazvania(self, aty):
        self.aty = aty
    
    def getnazvania(self):
        print(self.aty)

class Cat(Animal):
    def __init__(self, voice, color, breed):
        super().__init__(voice, color)
        self.breed = breed
        
        
    def giveVoice(self):
        print(self.legs, self.tail, self.voice, self.color, self.breed)

p1 = Animal("WOOF!!!", "GRAY")
p1.setnazvania("KOWKA")
p1.giveVoice()
p1.getnazvania()