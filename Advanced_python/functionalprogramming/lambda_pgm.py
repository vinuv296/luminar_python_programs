# in java we use camelin notatiom like addTwonumbers
# in python we use snake notatio like add_twonumbers
#lambda functions

def add(num1,num2):
    return num1+num2
print(add(10,20))

add=lambda num1,num2:num1+num2
print(add(100,200))

cube=lambda num:num**3
print(cube(2))
