n=int(input("Enter a number"))
s=0
num=0
while(n>0):
    s=n%10
    num=s+num*10
    n=n//10
print(num)
