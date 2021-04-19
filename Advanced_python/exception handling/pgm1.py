# a=int(input("Enter a first number"))
# b=int(input("Enter  second number"))
# try:#write code that might lead to exception
#     c=a/b
#     print(c)
# except:#if exception occured except block will be called
#     print("Exception occured")

#division by zero exception
#Index out of bound exception
#Invalid literal for input

a=[1,23,4,5,6]
try:
    print(a[8])
except Exception as e:
    print(e)

try:
    print(a[9])
except Exception as d:
    print("Exception occured")

try:
    n1=int(input("Enter a num"))
except Exception as e:
    print(e)

try:
    print(a[3])
except Exception as e:
    print(e)
finally:
    print("inside finally")
