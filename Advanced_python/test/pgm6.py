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
f=open("test_file",'r')
c=[]
for i in f:
    data=i.split(",")
    nam=data[0]
    rol=data[1]
    cr=data[2]
    mar=int(data[3])
    c.append(mar)
    max_val=max(c)
    if mar==max_val:
         ob=Student(nam,rol,cr,mar)
         ob.print_val()
