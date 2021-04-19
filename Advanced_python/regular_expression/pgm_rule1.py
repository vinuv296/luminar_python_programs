# import  re
# n="hello"
# x='\w{5}' # word with 5 letters
# m=re.fullmatch(x,n)
# if m is not None:
#     print("valid")
# else:
#     print("invalid")

import  re
n="56kg"
x='\d{2}\w{2}' # word with 5 letters \d{2}[a-z]{2}
m=re.fullmatch(x,n)
if m is not None:
    print("valid")
else:
    print("invalid")