class Employee:
    cmpy='KNM'
    def emep(self,name,id,sal):
        self.n=name
        self.i=id
        self.s=sal
    def prnt(self):
        print(self.n)
        print(self.i)
        print(self.s)
        print(Employee.cmpy)
    def __str__(self):
        return str(self.i)
d=Employee()
d.emep('giju',456,4500)
print(d)