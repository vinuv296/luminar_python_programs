f=open("/Users/HP/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(" ")
print(data)

    # fname=data[2]
    # age=data[3]
    # loc=data[-1]
    # print(fname,",",age,",",loc)


    #count the number people in one location
    #count number of people in age
    #count number of people based on profession