class Name:
    slno=123
    def details(self,name,addr,phone):
        self.na=name
        self.ad=addr
        self.ph=phone
class Employee(Name):
    def print(self):
        print("slno-",Name.slno)
        print("Name-",self.na)
        print("Address-",self.ad)
        print("Phone-",self.ph)
ob=Employee()
ob.details('vinu','Ajayabhavna,Kottayam',8978543982)
ob.print()

