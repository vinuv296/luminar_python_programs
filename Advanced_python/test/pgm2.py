
class Person:
    name = 'Raj'
    def m1(self, age):
        self.age = age
        print("name is ", Person.name)
        print(self.age)
class Address(Person):
    def m3(self,addr,phone):
        self.addr=addr
        self.phone=phone
        print("age-",self.age)
class Details(Address):
    def m2(self):
        print(self.age)
        print(self.addr)
        print(self.phone)
c = Details()
c.m1(21)
c.m3("House No-123,abcd dist,kerala",1111111)
c.m2()
