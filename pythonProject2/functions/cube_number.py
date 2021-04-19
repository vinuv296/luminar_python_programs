def cube_number():
    num=int(input("Enter a number"))
    c=num**3
    print("cube",c)
cube_number()


def cube_number(num1):
    c=num1*num1*num1
    print("Cube -",c)
cube_number(int(input("Enter a number")))




def cube_number(num1):
    c=num1*num1*num1
    return c
num=int(input("Enter a number"))
res=cube_number(num)
print(res)
