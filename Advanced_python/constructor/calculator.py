class Calculator:
    def __init__(self,n1,n2):
        self.no1=n1
        self.no2=n2
    def add(self):
        self.r=self.no1+self.no2
        print("Sum of two number-",self.r)
    def diff(self):
        self.r=self.no1-self.no2
        print("Difference of two number-",self.r)
    def prod(self):
        self.r=self.no1*self.no2
        print("product of two numbers-",self.r)
    def div(self):
        self.r=self.no1/self.no2
        print("Division-",self.r)
ob=Calculator(56,5)
ob.add()
ob.diff()
ob.prod()
ob.div()

