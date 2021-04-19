# class Bank:
#     def accCreate(self,accno,name):
#         self.name=name
#         self.acc_no=accno
#         self.mini_bal=2500
#         self.balance=self.mini_bal
#     def deposite(self,amt):
#         self.balance+=amt
#         print("Amount deposited and total balance",self.balance)
#     def withdraw(self,amt):
#         if amt>self.balance:
#             print("insuffiencet balanve")
#         else:
#             print("account debited",amt)
#             self.balance+=amt
#             print("Total balance",self.balance)
# b=Bank()
# b.accCreate(112,'binu')
# b.deposite(5000)
# b.withdraw(2000)
#types of variable
#1.instance variable .....related to object
#2. static variable....related to class
#.......................can access using class name
class Bank:
    bname="sbi"#static variable
    def accCreate(self,accno,name):
        self.name=name
        self.acc_no=accno
        self.mini_bal=2500
        self.balance=self.mini_bal
    def deposite(self,amt):
        self.balance+=amt
        print("Amount deposited and total balance",self.balance,"at branch",Bank.bname)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insuffiencet balanve")
        else:
            print("account debited",amt)
            self.balance+=amt
            print("Total balance",self.balance)
b=Bank()
b.accCreate(112,'binu')
b.deposite(5000)
b.withdraw(2000)
