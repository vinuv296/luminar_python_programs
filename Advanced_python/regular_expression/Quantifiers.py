# import  re
#
# x="a+" # a including group
# r="aaa abc ahe erga"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


#
# import re
# x="a*" # a including group and without a and without a group
# r="aaaa fga"
# mat=re.finditer(x,r)
# for i in mat:
#     print(i.start())
#     print(i.group())

#
# import re
# x="a?" # a return postion with a
# r="aaaa fga"
# mat=re.finditer(x,r)
# for i in mat:
#     print(i.start())
#     print(i.group())



#
# import re
# x="a{5}" # no of consecutive position of a
# r="aaaa aaaaafg"
# mat=re.finditer(x,r)
# for i in mat:
#     print(i.start())
#     print(i.group())



# import re
# x="a{1,3}" # a minimum 1 and maximum 3
# r="aaaafgaa"
# mat=re.finditer(x,r)
# for i in mat:
#     print(i.start())
#     print(i.group())



# import re
# x="^a" # a check starting with a
# r="aaaa fga"
# mat=re.finditer(x,r)
# for i in mat:
#     print(i.start())
#     print(i.group())



import re
x="a$" # check ending with a
r="aaaa fga"
mat=re.finditer(x,r)
for i in mat:
    print(i.start())
    print(i.group())