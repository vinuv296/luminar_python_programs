# def sub(num1,num2):
#     if num1<num2:
#         (num1,num2)=(num2,num1)
#     return num1-num2
# res=sub(10,20)
# print(res)

# here we want subtract a lowest value from a highest value all time even though the parameter order are different
# here we use a decorate


def decorator_sub(fuct):
    def inner(num1,num2):
        (num1,num2)=(num2,num1)
        return fuct(num1,num2)
    return inner
@decorator_sub
def sub(num1,num2):
    return num1-num2
res=sub(20,100)
print(res)
