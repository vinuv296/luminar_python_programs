# import re
# a=input("Enter a number")
# r='\d{10}'
# m=re.fullmatch(r,a)
# if m is not None:
#     print("valid",m)
# else:
#     print("Invalid",m)


import re
a=input("Enter a number")
#r='^[+91]\d{10}'
r='[+][9][1]\d{10}'
m=re.fullmatch(r,a)
if m is not None:
    print("valid")
else:
    print("Invalid")