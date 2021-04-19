lst=[10,20,56,3,5,8,9,112]
even=list(filter(lambda num:num%2==0,lst))
print(even)

names=["manu","rajeev","rahuk","anand","arya","arun"]
a_names=list(filter(lambda n:n[0]=='a',names))
print(a_names)
