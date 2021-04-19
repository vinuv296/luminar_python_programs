class Student:
    def __init__(self,name,roll,crs,mark):
        self.n=name
        self.r=roll
        self.c=crs
        self.m=mark
    def print_val(self):
        print("name-",self.n)
        print("Roll-",self.r)
        print("Course",self.c)
        print("Mark",self.m)
        print("............")
f=open("studentdetails",'r')
for i in f:
    data=i.split(",")
    nam=data[0]
    rol=data[1]
    cr=data[2]
    mar=int(data[3])
    if mar>190:
        ob=Student(nam,rol,cr,mar)
        ob.print_val()
