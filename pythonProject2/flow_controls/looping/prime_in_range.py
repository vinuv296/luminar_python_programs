num1=int(input("Enter lower limit"))
num2=int(input("Enter upper limit"))
for i in range(num1,num2):
    for j in range(2,i,1):
        if(i%j!=0):
            print(i)

