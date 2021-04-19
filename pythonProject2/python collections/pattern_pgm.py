pattern="ABDEHGB"
dist={}
for i in pattern:
    if i in dist:
        print("first recursive character -",i)
        break
    else:
        dist[i]=1
