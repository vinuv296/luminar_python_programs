#nested List
employee=[[1,"arjun",10000],[2,"manju",14000],[3,"jeffin",250000]]
print(employee)
for i in employee:
    print(i)
for i in employee:
    print(i[1])
for k in employee:
    if i[2]>17000:
        print(i[1])
        break
sal=0
for m in employee:
    sal=sal+m[2]
print(sal)