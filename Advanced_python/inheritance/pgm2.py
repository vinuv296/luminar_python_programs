class Person:
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def printval(self):
        print("name-",self.nam)
        print("age-",self.ag)
class Student(Person):
    def __init__(self,roll,mark,name,age):
        super().__init__(name,age)
        self.r=roll
        self.m=mark
    def prt(self):
        print(self.r)
        print(self.m)
ob=Student(2,75,'hai',20)
ob.printval()
ob.prt()
