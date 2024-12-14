f = open("./input/day11.txt", "r")
safecount=0
lines=f.readlines()

result1=0
numlist=lines[0].split(' ')

for x in range(len(numlist)):
    numlist[x]=int(numlist[x])


def blink(num):
    newlist=[]
    t=num
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

cachedir=[]
cache=[]

for n in numlist:
    cachedir.append(n)
    cache.append(1)

for x in range (75):
    currentcachedir=cachedir.copy()
    currentcache=[]
    xn=len(currentcachedir)
    currentcache=[0]*xn

    for i in range (len(cachedir)):
        x=cachedir[i]
        oldoccur=cache[i]
        if oldoccur==0:
            continue
        newl=blink(x)
        newnoindex=-1
        for t in newl:
            try:
                newnoindex=currentcachedir.index(t)
            except:
                currentcachedir.append(t)
                currentcache.append(0)
                newnoindex=len(currentcachedir)-1
            currentcache[newnoindex]+=oldoccur
    cachedir=currentcachedir.copy()
    cache=currentcache.copy()
                      


for x in cache:
    result1+=x
print("Result for part 1 is ....", result1)