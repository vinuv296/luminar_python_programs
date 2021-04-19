# some function in python
#input
#print
#type

#normal type

# def functionname(arguments):
#     fuction definition
#
# function call #using fn name

# Three methods for define functions in python
#
# 1.Function without an arguments and no returm type
# 2.Function with arguments and no return type
# 3.Function with arguments and return type

#1. Method
# def mul_sub():
#     num1=int(input("Enter 1st number"))
#     num2=int(input("Enter 2nd number"))
#     sub=num1-num2
#     print("result after substraction ",sub)
#     mul=num1*num2
#     print("result after multiplication ",mul)
# mul_sub()

#2.Method
# def add(num1,num2):
#     sum=num1+num2
#     sub=num1-num2
#     print("sum-",sum)
#     print("sub",sub)
# add(20,10)

# 3.Method
def sum(num1,num2):
    sum=num1+num2
    diff=num1-num2
    return sum
data=sum(15,25)

print(data)

