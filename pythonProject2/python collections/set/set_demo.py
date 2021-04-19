#set

# set1={}
# print(type(set1))
#if {} is written it will create a dictionary

#to create an empty set use set() function or with {} curly braces with values

# set1=set()
# or
# set1={1,2,3,4}

# set2={1,3.6,True,"Vinu"}# support heterogenous value.....True='1'....it support boolean values but doesnot support duplicate values
# print(set2)
#
# set3={1,2,3,4,2,1,3}#duplication of values is not allowed
# print(set3)
#
# set4={1,3,4,5,7,8,10.4,"sanju,minu,jebin"}#insertion order is not preserved
# print(set4)
#
# set4[3]=100
# print(set4)


# #add an element into set............add
# set5={1,3,4}
# set5.add(8)
# set5.add("Luminar")
# print(set5)
#
#
# #add multiple element into a set.................update
# set5.update([50,56])
# print(set5)


#sum()
#max()
#min()
#len()

# set8=[1,2,3]
# print(sum(set8))
# print(max(set8))
# print(min(set8))
# print(len(set8))


#set Operations
#union
#intersection
#Difference

set1={1,2,3,4,5,6}
set2={5,6,8,9}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)
set6=set1.difference(set2)
print(set6)
set7=set2.difference(set1)
print(set7)