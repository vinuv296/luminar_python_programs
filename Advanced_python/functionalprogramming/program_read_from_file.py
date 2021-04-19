class Employee:
    def __init__(self,eid,name,desgn,sal):
        self.eid=eid
        self.name=name
        self.desgn=desgn
        self.sal=sal

f=open("employees")
employees=[]
for lines in f:
    eid,name,desgn,sal=lines.rstrip("\n").split(",")
    e=Employee(eid,name,desgn,sal)
    employees.append(e)
salaries=list(map(lambda emp:emp.salary,employees))
print(salaries)