import re
x="[abc]" # either a,b,c
matcher=re.finditer(x,"abt c@4kytrc")
for i in matcher:
    print(i.start())
    print(i.group())


import re
x="[^abc]" # except a b c
matcher=re.finditer(x,"abt c@4kytrc")
for i in matcher:
    print(i.start())
    print(i.group())
print("..................")
import re
x="[0-9]" # either a,b,c
matcher=re.finditer(x,"abt c@4kytrc")
for i in matcher:
    print(i.start())
    print(i.group())
print("..........................")
import re
x="\s"
matcher=re.finditer(x,"abt c@4kytrc")
for i in matcher:
    print(i.start())
    print(i.group())

import re
x="\w"
matcher=re.finditer(x,"abt c@4kytrc")
for i in matcher:
    print(i.start())
    print(i.group())