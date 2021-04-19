l=[]
e=[]
o=[]
for i in range (50,101):
    l.append(i)
print("Original list",l)
for j in l:
    if j%2==0:
        e.append(j)
    else:
        o.append(j)
print("Even number list-",e)
print("Odd number list-",o)