num1=int(input("Enter lower limit"))
num2=int(input("Enter upper limit"))
sum_e=0
sum_o=0
for i in range(num1,num2+1,1):
    if(i%2==0):
        sum_e+=i
    else:
        sum_o+=i
print("sum of odd numbers",sum_o)
print("sum of even numbers",sum_e)