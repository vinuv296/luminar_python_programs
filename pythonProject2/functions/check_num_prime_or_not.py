def prime_or_not():
    n=int(input("Enter a number"))
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=1
    if(c==0):
        print("not a Prime number")
    else:
        print("prime number")
prime_or_not()