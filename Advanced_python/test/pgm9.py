import re
x="[A-Z]+[a-z]+$" # check ending with a
r="Indian Is World of Culture"
#r="abc"
mat=re.finditer(x,r)
if mat is not None:
    print("valid")
else:
    print("invalid")
