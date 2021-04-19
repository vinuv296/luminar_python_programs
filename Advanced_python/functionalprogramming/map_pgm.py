# map()
# filter()
# reduce()

# pass two arguments
#1st arg is  which function want to applied
#2st arg mention iterable object(list,set etc)



lst=[10,20,30,40]
squ=[]
for num in lst:
    res=num**2
    squ.append(res)
print(squ)


#..............................

lst=[1,2,3,4,5,6]
def squ(no):
    return no**2
square=list(map(squ,lst))
print(square)

#...............................

squ1=list(map(lambda no:no**2,lst))
print(squ1)

#....................................

cub=list(map(lambda no:no**3,lst))
print(cub)

#...................................

