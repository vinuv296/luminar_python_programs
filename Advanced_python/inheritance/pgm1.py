#inheritence child class can inherit parent class by "class Child(Parent)"

#............Single Inheritance.....

class Parent:
    parent_name='Rajeev'
    def m1(self,age):
        self.age=age
        print("name is ",Parent.parent_name)
        print(self.age)
class Child(Parent):
    def m2(self):
        print("Parent name-",Parent.parent_name)
        print(self.age)
c=Child()
c.m1(21)
c.m2()

#.............multiple inheritance.........

class Parent:
    parent_name='Rajeev'
    def m1(self,age):
        self.age=age
        print("name is ",Parent.parent_name)
        print(self.age)
class Mobile:
    def mob(self):
        print("I have a small mobile")
class Child(Parent,Mobile):
    def m2(self):
        print("Parent name-",Parent.parent_name)
        print(self.age)
c=Child()
c.m1(21)
c.m2()
c.mob()
print("...........")

#..................Multi level Inheritance...OR Hierarchial inheritance..........
class Parent:
    parent_name='Rajeev'
    def m1(self,age):
        self.age=age
        print("name is ",Parent.parent_name)
        print(self.age)
class Child(Parent):
    def m2(self):
        print("Parent name-",Parent.parent_name)
        print(self.age)
class child_details(Child):
    def m3(self):
        print("Child inherited")

c=child_details()
c.m1(21)
c.m2()
c.m3()
print("......")
o=Child()
o.m1(25)
o.m2()
