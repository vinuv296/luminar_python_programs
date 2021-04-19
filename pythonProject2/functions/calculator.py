print("Choose your option")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Division")
ch=int(input("Enter your choice"))
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
def add_1(num1,num2):
    sum_res = num1 + num2
    return sum_res
def sub(num1,num2):
    sub_res=num1-num2
    return sub_res
def mul(num1,num2):
    mul_res=num1*num2
    return mul_res
def div(num1,num2):
    div_res=num1/num2
    return  div_res

if(ch==1):
    data=add_1(num1,num2)
    print("Result=",data)
elif(ch==2):
    print("Result=",sub(num1,num2))
elif(ch==3):
    data = mul(num1, num2)
    print("Result=", data)
elif(ch==4):
    data = div(num1, num2)
    print("Result=", data)
else:
    print("invalid choice")