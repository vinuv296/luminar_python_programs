def fact():
    n=int(input("Enter a number"))
    val=1
    for i in range(1,n+1):
        val=i*val
    print("Factorial",val)
fact()

def fact(num1):
    val=1
    for i in range(1,num1+1):
        val=i*val
    print("Factorial",val)
fact(int(input("Enter a value")))

def fact(num1):
    val=1
    for i in range(1,num1+1):
        val=i*val
    return val
data=fact(5)
print("Factorial",data)