class Animal:
    def __init__(self, name, age):
        self.nam = name
        self.ag = age

    def printval(self):
        print("name-", self.nam)
        print("age-", self.ag)

class Dog(Animal):
    def __init__(self, type,name, age):
        super().__init__(name, age)
        self.type = type

    def prt(self):
        print(self.type)

ob = Dog("pet","Kutu",20)
ob.printval()
ob.prt()