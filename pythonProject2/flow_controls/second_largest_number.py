num1=int(input("Enter 1st num"))
num2=int(input("Enter 2nd num"))
num3=int(input("Enter 3rd num"))
if(num1>num2 & num1>num3):
    if(num2>num3):
        print(num2,"is second largest number")
    else:
        print(num3,"is second largest number")
elif(num2>num1 & num2>num3):
    if(num1>num3):
        print(num1, "is second largest number")
    else:
        print(num3, "is second largest number")
