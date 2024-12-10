import copy
import array
f = open("./input/day10.txt", "r")
safecount=0
lines=f.readlines()

xcount=0
ycount=0
xmax=0
ymax=0
result=0
coordinates =[]
user=[0,0]
trailends=[]
dtrailends=[]

def Move(p, index, l):
    global result
    x=p.x
    y=p.y
    val=p.v

    if val==9:
        trail=l[0],index
        dtrail=l.append(index)
        if(trail not in trailends):
            trailends.append(trail)
        if(dtrail not in dtrailends):
            dtrailends.append(trail)        
        return

    #MoveLeft
    next=index-1
    if(x>0 and next not in l and coordinates[next].v==val+1):
        t=l.copy()
        t.append(next)
        Move(coordinates[next], next, t)
    #MoveRight
    next=index+1
    if(x<xmax and next not in l and coordinates[next].v==val+1):
        t=l.copy()
        t.append(next)
        Move(coordinates[next], next, t)
    #MoveDown
    next=index+xmax+1
    if(y<ymax and next not in l and coordinates[next].v==val+1):
        t=l.copy()
        t.append(next)
        Move(coordinates[next], next, t)
    #MoveUp
    next=index-(xmax+1)
    if(y>0 and next not in l and coordinates[next].v==val+1):
        t=l.copy()
        t.append(next)
        Move(coordinates[next], next, t)


class Point:
    def __init__(self, x, y, v):
        self.x=x
        self.y=y
        self.v=v

for t in lines:
    for c in t:
        if(c=='\n'):
            break
        if(c=='.'):
            c=-1
        temp=Point(xcount, ycount, int(c))
        xcount+=1
        coordinates.append(temp)
    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1

startingpoints=[]

i=0
for c in coordinates:
    if c.v==0:
        startingpoints.append(i)
    i+=1

for s in startingpoints:
    l=[s]
    p=coordinates[s]
    Move(p, s, l)

result = len(trailends)
result2=len(dtrailends)

print ("Part 1 is ......" ,result)
print ("Part 2 is ......" ,result2)