#employee
#id,name,designation,salary(Key,value)
#1.Print employee
#2.Company name print
#3.Addsany Luminar and Print salar 15000
#4.print all key value pairs


emp={"id":1,"name":"arun","desg":"manager","sal":1200}
print(emp)
print(emp["name"])
print("company" in emp)
emp["company"]="luminar"
emp["sal"]=150000
for i in emp:
    print(i,":",emp[i])