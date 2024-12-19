f = open("./input/day19.txt", "r")
lines=f.readlines()

towels=[]
reqs=[]
result1=0
result2=0

for i in range(len(lines)):
    if(i==0):
        towels=lines[i].split(',')

    else:
        if(lines[i]=="\n"):
            continue
        reqs.append(lines[i].strip('\n'))

for r in reqs:
    activelist=[]
    for t in towels:
        activelist.append(t)
    templist=[]
    while(len(activelist)>0):
        temp=activelist.pop(0)
        length=len(temp)
        if(r[:length]==temp):
            templist.append(temp)
            if(temp==r):
                result1+=1
            else:
                for t in towels:
                    activelist.append(temp+t)
        for a in activelist:
            for t in towels:
                temp=(a+t).replace(" ", "")
                length=len(temp)
                if(r[:length]==temp):
                    templist.append(temp)
                    if(temp==r):
                        result1+=1
                    break
        activelist=templist.copy()

print("The result for pt 1 is: ", result1)
