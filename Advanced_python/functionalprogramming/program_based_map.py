class Employee:
    def __init__(self,eid,ename,desgn,salary):
        self.eid=eid
        self.ename=ename
        self.desgn=desgn
        self.salary=salary
    def print_emp(self):
        print(self.ename)
em1=Employee(123,"gigu","sales",15000)
em2=Employee(1234,"manu","sale",56666)
em3=Employee(1563,"jinu","marketing",80000)
employees=[]
employees.append(em1)
employees.append(em2)
employees.append(em3)
#sal=[]
#for j in employees:
#   sal.append(j.salary)
#print(sal)

salary=list(map(lambda emp:emp.salary,employees))
print(salary)
