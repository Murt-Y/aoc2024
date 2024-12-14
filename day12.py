f = open("./input/day12.txt", "r")
lines=f.readlines()

class Point:
    def __init__(self, x, y, v, check):
        self.x=x
        self.y=y
        self.v=v
        self.check=check


xcount=0
ycount=0
xmax=0
ymax=0
result1=0
result2=0
coordinates =[]

cachedir=[]
cache=[]

for t in lines:
    for c in t:
        if(c=='\n'):
            break
        temp=Point(xcount, ycount, c, False)
        try:
            cindex=cachedir.index(c)
        except:
            cachedir.append(c)
            cindex=len(cachedir)-1
            cache.append([])
        xcount+=1
        coordinates.append(temp)
    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1


def Check(p, index):
    x=p.x
    y=p.y
    val=p.v
    area=[index]
    temp=[]
    fence=0
    p.check=True
    #Checkleft
    next=index-1
    if(x>0  and coordinates[next].v==val):
        if( coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]

    else:
        fence+=1
    #CheckRight
    next=index+1
    if(x<xmax  and coordinates[next].v==val):
        if(coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
    else:
        fence+=1
    #CheckDown
    next=index+xmax+1
    if(y<ymax  and coordinates[next].v==val):
        if(coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
    else:
        fence+=1
    #CheckUp
    next=index-(xmax+1)
    if(y>0  and coordinates[next].v==val):
        if(coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
    else:
        fence+=1
    return area,fence

i=0
for c in coordinates:
    if(c.check==False):
        temp=[]
        index=0
        try:
            group=cachedir.index(c.v)
        except:
            cachedir.append(c.v)
            group=len(cachedir)-1
        temp=Check(c, i)
        area=temp[0]
        fence=temp[1]
        cache[group].append(area)
        result1+=(fence*len(area))

    i+=1


print("Result 1 is ..." , result1)