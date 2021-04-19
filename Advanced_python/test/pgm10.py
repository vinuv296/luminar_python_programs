# import re
# x='^a+[a-zA-A]+b$' # check ending with a
# r="antb"
# mat=re.fullmatch(x,r)
# if mat is not None:
#     print("valid")
# else:
#     print("invalid")


import re
x='[A-Z]+[a-z]+$' # check ending with a
r="Geva"
mat=re.fullmatch(x,r)
if mat is not None:
    print("valid")
else:
    print("invalid")