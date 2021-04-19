#class : design pattern
#object : real world entity
#references : name that refers a memory location of a object


class Person:
    def walk(self):
        print("person is walking")
    def run(self):
        print("person is running")
    def jump(self):
        print("person is jumping")
obj=Person()
obj.walk()
obj.run()
obj.jump()

ab=Person()
ab.walk()

class Person1:
    def setVal(self,name,age):
        self.age=age
        self.name=name
    def printval(self):
        print("name",self.name)
        print("age",self.age)
odj=Person1()
odj.setVal('rzm',23)
odj.printval()
