line="hai hello hai hello hai"
print(line)
word=line.split(" ")
print(word)
dist={}
for i in word:
    if i in dist:
        dist[i]+=1
    else:
        dist[i]=1
for j in dist:
    print(j,":",dist[j])

# if i not in dist or if i in dist
