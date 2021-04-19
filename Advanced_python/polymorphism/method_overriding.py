class Parent:
    def properties(self):
        print("10 lakh rs,2 Car")
    def mary(self):
        print("with raju")
class Child(Parent):
    def mary(self):
        print("With Gopi")
c=Child()
c.mary()