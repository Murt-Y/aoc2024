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

def RotareR(dir):
    if dir==0:
        return 1
    elif dir==1:
        return 2
    elif dir==2:
        return 3
    else:
        return 0
    
def RotareL(dir):
    if dir==0:
        return 3
    elif dir==1:
        return 0
    elif dir==2:
        return 1
    else:
        return 2


def Check(p, index):
    x=p.x
    y=p.y
    val=p.v
    area=[index]
    temp=[]
    fence=0
    fenceh=[]
    fencev=[]
    p.check=True
    #Checkleft
    next=index-1
    if(x>0  and coordinates[next].v==val):
        if( coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
            fenceh=list(set(fenceh+temp[2]))
            fencev=list(set(fencev+temp[3]))

    else:
        fence+=1
        newfence=(x,y)
        if(newfence not in fencev):
            fencev.append(newfence)
    #CheckRight
    next=index+1
    if(x<xmax  and coordinates[next].v==val):
        if(coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
            fenceh=list(set(fenceh+temp[2]))
            fencev=list(set(fencev+temp[3]))
    else:
        fence+=1
        newfence=(x+1,y)
        if(newfence not in fencev):
            fencev.append(newfence)
    #CheckDown
    next=index+xmax+1
    if(y<ymax  and coordinates[next].v==val):
        if(coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
            fenceh=list(set(fenceh+temp[2]))
            fencev=list(set(fencev+temp[3]))
    else:
        newfence=(x,y+1)
        if(newfence not in fenceh):
            fenceh.append(newfence)
        fence+=1
    #CheckUp
    next=index-(xmax+1)
    if(y>0  and coordinates[next].v==val):
        if(coordinates[next].check==False ):
            temp=Check(coordinates[next], next)
            area+=temp[0]
            fence+=temp[1]
            fenceh=list(set(fenceh+temp[2]))
            fencev=list(set(fencev+temp[3]))
    else:
        newfence=(x,y)
        if(newfence not in fenceh):
            fenceh.append(newfence)
        fence+=1
    return area,fence, fenceh, fencev

def checkH(fenceh, fencev):
    fencelines=0
    for i in range (ymax+2):
        list_of_lines = list(filter(lambda t: t[1] == i, fenceh))
        list_of_lines.sort()
        lastindex=-2
        for t in list_of_lines:
            if(t[0]-lastindex!=1):
                fencelines+=1
            elif((t[0],t[1]-1)in fencev and (t[0],t[1])in fencev):
                fencelines+=1
            lastindex=t[0]
    return fencelines

def checkV(fencev, fenceh):
    fencelines=0
    for i in range (xmax+2):
        list_of_lines = list(filter(lambda t: t[0] == i, fencev))
        list_of_lines.sort()
        lastindex=-2
        for t in list_of_lines:
            if(t[1]-lastindex!=1):
                fencelines+=1
            elif((t[0]-1,t[1])in fenceh and (t[0],t[1])in fenceh):
                fencelines+=1
            lastindex=t[1]
    return fencelines

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
        fenceh=temp[2]
        fencev=temp[3]
        horlines=checkH(fenceh, fencev)
        verlines=checkV(fencev, fenceh)
        cache[group].append(area)
        result1+=(fence*len(area))
        result2+=((horlines+verlines)*len(area))

    i+=1





print("Result 1 is ..." , result1)
print("Result 2 is ..." , result2)