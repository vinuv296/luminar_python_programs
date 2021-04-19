# Pattern Matching

# RE=Package for pattern matching

import re
count=0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    count+=1
print("count",count)


import re
c=0
matche=re.finditer('ab','abaabbab')
for i in matche:
    print("Match available at",i.start())   #return positions
    print("Group-",i.group())   # which object find match
    c+=1
print("count-",c)
