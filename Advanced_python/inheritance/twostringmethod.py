class College:
    collegename='SRM'
    def __init__(self,name,roll):
        self.r=roll
        self.n=name
    def printDetails(self):
        print("colg name",self.collegename)
        print("name",self.n)
        print("roll",self.r)
    def __str__(self):
        #return self.n#....This toString method will only retrun a string value....if you want to return an integer value
    #you have to convert it to string
        return  self.n+str(self.r)

o=College('hema',34)
print(o)
