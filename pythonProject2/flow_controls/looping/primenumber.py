num=int(input("Enter a number"))
c=0
for i in range(2,num-1):
    if(num%i==0):
        c=c+1
if(c>0):
    print("prime number")
else:
    print("Not a prime number")