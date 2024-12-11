f = open("./input/day11.txt", "r")
safecount=0
lines=f.readlines()

result1=0
numlist=lines[0].split(' ')

for x in range(len(numlist)):
    numlist[x]=int(numlist[x])


def blink(numlist):
    newlist=[]
    for t in numlist:
        ts=str(t)
        if(t==0):
            newlist.append(1)
        elif(len(ts)%2==0):
            m=int(len(ts)/2)
            m1=int(ts[:m])
            m2=int(ts[m:])
            newlist.append(m1)
            newlist.append(m2)
        else:
            t=t*2024
            newlist.append(t)
    return newlist

for x in range (25):
    updatelist= blink(numlist)
    numlist=updatelist.copy()

result1=len(numlist)
print("Result for part 1 is ....", result1)