lst=[4,2,1,6,7,8]
#output [3,1,0,7,8,9]

new_list=[]
for i in lst:
    if(i<5):
        i-=1
        new_list.append(i)
    else:
        i+=1
        new_list.append(i)
print(new_list)
#............................................

out=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(out)

#...........................................

# if num<5:
#      return num-1
# else:
#      return num+1

#...........................................
