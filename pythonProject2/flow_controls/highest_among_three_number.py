num1=int(input("Enter 1st num"))
num2=int(input("Enter 2nd num"))
num3=int(input("Enter 3rd num"))
if(num1>num2 & num1>num3):
    print(num1,"is greater than",num2 ,"and",num3)
elif(num2>num3):
    print(num2,"is greater than",num1 ,"and",num3)
else:
    print(num3, "is greater than", num1,"and", num2)