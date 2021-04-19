def print_person_details(**data):
    print(data)
print_person_details(name="vinu",birthpalce="kottayam",workplace="ernakulam")

def add(*args):
    sum=0
    for num in args:
        sum+=sum
    return sum
res=add(10,20,3,5,56,80)
print(res)

#...............................................................

mployee={1000:{"name":"sanjay","design":"pythontrainer","exp":3},
         1001:{"name":"sabir","design":"bigdata","exp":3},
         1002:{"name":"christy","design":"ML","exp":3}
         }

eid=int(input("Enter an employee id"))
if(eid in mployee):
    print(mployee[eid])
    print(mployee[eid]["name"])
else:
    print("eid not exist")

#...................................................

def emp_details(**data):
    eid=data["eid"]
    propty=data["prop"]
    if eid in mployee:
        print(mployee[eid]["name"])
        print(mployee[eid][propty])
    else:
        print("eid not in the dictionary")

r=emp_details(eid=1000,prop="design")

#.....................................................



