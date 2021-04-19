f=open("numbers","r")
list_even=[]
list_odd=[]
for i in f:
    if int(i)%2==0:
        list_even.append(int(i.rstrip("\n")))
    else:
        list_odd.append(int(i.rstrip("\n")))
print(list_odd)
print("sum of odd number list",sum(list_odd))
print(list_even)
print("sum of even number list",sum(list_even))