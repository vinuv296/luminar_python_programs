f=open("numbers","r")
list=[]
for i in f:
    list.append(int(i.rstrip("\n")))
print(list)
print(sum(list))

#\n
#....rstrip(" ") is used to remove end characters
#....lstrip(" ") is used to remove begining characters



