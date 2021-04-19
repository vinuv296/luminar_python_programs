class Employee:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def printv(self):
        print("name",self.n)
        print('age',self.a)
f=open("student",'r')
for l in f:
    data=l.split(",")
    name=data[0]
    age=data[1]
    ob=Employee(name,age)
    ob.printv()