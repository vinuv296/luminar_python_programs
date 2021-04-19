class Person:
    def show(self,num1):
        self.n1=num1
        print(self.n1)
class Student(Person):
    def show(self,num2,num3):
        self.n2=num2
        self.n3=num3
        print(self.n2,self.n3)
p=Student()
p.show(3,6)
# python does not support method overloading ....if we implement the last or most recent mathod will be called here show() with 2 arguments

