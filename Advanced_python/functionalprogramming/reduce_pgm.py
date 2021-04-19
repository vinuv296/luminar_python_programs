from functools import reduce
lst=[10,50,6,3,9,45]
tot=reduce(lambda no1,no2:no1+no2,lst)
print(tot)

high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)
