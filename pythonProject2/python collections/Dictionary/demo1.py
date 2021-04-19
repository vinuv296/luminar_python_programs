#Dictionary

d={}
print(type(d))

# value stored in dictionary as key-value pairs
#example
#roll:1001
#name:Arun
#$age:25

#key:roll,name,age

#1001,arun,25
student={"roll":1001,"name":"arun","age":25}#it support heterogenous value
print(student)
student1={"roll":1,"name":"arun","age":25,"age":30}
print(student1)# dictionary does not duplicate Key values
student2={"roll":1,"name":"arun","age":25,"Slno":25}# dictionary support duplicate value but not the Key
print(student2)# In Dictionary Insertion Order is Preserved

print(student2["age"])#fetch a particular value from a dictionary  by using corresponding key


for i in student1:
    print(i)
    print(i,":",student1[i])

#Update.....................IS MUTABLE
#..........................................

student1["name"]="vinu"
print(student1["name"])
student1["age"]=55
print(student1["age"])
student1["age"]+=10
print(student1["age"])

#Delete (del)
#.........................................
del student2["Slno"]
print(student2)

#.........................................

#search a Key in a Dictionary present or not
print("total" in student1)
print("name" in student1)
print("slno" in student2)


student1["total"]=150
print(student1)



