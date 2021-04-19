# constructor is used to initailize instance variables
# constructor automatically invoke when creating object

class Person:
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def printval(self):
        print("name-",self.nam)
        print("age-",self.ag)
ob=Person("Manu",15)
ob.printval()