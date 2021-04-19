f=open("text1.txt","r")
dic={}
for i in f:
    word=i.split(" ")
for j in word:
    if j in dic:
        dic[j]+=1
    else:
        dic[j]=1
for k in dic:
    print(k,":",dic[k])

#or word=i.rstrip("\n").split(" ")

