list=[]
print("Enter the distances covered by racers in Marathon (Kilometers) please \n(press q to terminate):")
for i in range(1000):
    n=input()
    if n=='q':
        break
    else:
        list.append(n)
print(list)
print(len(list))
# p=['5', '8', '9', '56', '0', '2', '3', '5', '48', '789', '589', '659', '2000']
# for i in range(len(p)-1):
#     for j in range(len(p)-1):
#         if p[j]>p[j+1]:
#             p[j],p[j+1]=p[j+1],p[j]
# print(p)
