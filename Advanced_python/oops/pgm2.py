class Employee:
    cname='Capegemini'
    def emplydetails(self,eid,ename,edesign,esal):
        self.eid=eid
        self.enam=ename
        self.edesg=edesign
        self.sal=esal
    def printdetails(self):
        print("employee id",self.eid)
        print("employee name",self.enam)
        print("employee design",self.edesg)
        print("employee salary",self.sal)
        print("Company name -",Employee.cname)
em=Employee()
em.emplydetails(1,'name1','manager',250)
em.printdetails()


