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
global firstmove
firstmove=True

def Move(p, index, list, dir):
    global firstmove
    if(index==firstindex and dir==0):
        if firstmove==True:
            firstmove=False
        else:
            return 0

    x=p.x
    y=p.y
    next=0
    fence=0

    if(dir==0):
        #sağa doğru geldiyse önce yukarı bak varsa yönü yukarı dön yukarı git
        next=index-(xmax+1)
        if(y>0 and next in list):
            fence+=1
            dir=3
            fence+= Move(coordinates[next], next, list, dir)
        #yukari yoksa saga bak sagda varsa ona gec fence artmiyor
        else:
            next=index+1
            if(x<xmax and next in list):
                fence+=Move(coordinates[next], next, list, dir)
            #yan yoksa yönü aşağıya dön    
            else:
                fence+=1
                dir=1
                next=index+xmax+1
                if (y<ymax and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                #aşağı da yoksa geri sola dön
                else:
                    next=index-1
                    fence+=1
                    dir=2
                    fence+=Move(coordinates[next], next, list, dir)
    elif(dir==1):
        #aşağıya doğru geldiyse önce sağa bak varsa yönü sağa dön sağa git
        next=index+1
        if(x<xmax and next in list):
            fence+=1
            dir=0
            fence+= Move(coordinates[next], next, list, dir)
        #sağ yoksa aşağıya varsa ona gec fence artmiyor
        else:
            next=index+xmax+1
            if(y<ymax and next in list):
                fence+=Move(coordinates[next], next, list, dir)
            #aşağı yoksa yönü sola dön    
            else:
                fence+=1
                dir=2
                next=index-1
                if (x>0 and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                #sol da yoksa geri yukarı dön
                else:
                    next=index-(xmax+1)
                    fence+=1
                    dir=3
                    fence+=Move(coordinates[next], next, list, dir)
    if(dir==2):
        #sola doğru geldiyse önce aşağıya bak varsa yönü aşağı dön aşağı git
        next=index+(xmax+1)
        if(y<ymax and next in list):
            fence+=1
            dir=1
            fence+= Move(coordinates[next], next, list, dir)
        #aşağı yoksa sola bak solda varsa ona gec fence artmiyor
        else:
            next=index-1
            if(x>0 and next in list):
                fence+=Move(coordinates[next], next, list, dir)
            #yan yoksa yönü yukar dön    
            else:
                fence+=1
                dir=3
                next=index-(xmax+1)
                if (y>0 and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                #yukarı da yoksa geri sağa dön
                else:
                    next=index+1
                    fence+=1
                    dir=0
                    fence+=Move(coordinates[next], next, list, dir)
    elif(dir==3):
        #yukar doğru geldiyse önce sola bak varsa yönü sola dön sola git
        next=index-1
        if(x>0 and next in list):
            fence+=1
            dir=2
            fence+= Move(coordinates[next], next, list, dir)
        #sol yoksa yukar varsa ona gec fence artmiyor
        else:
            next=index-(xmax+1)
            if(y>0 and next in list):
                fence+=Move(coordinates[next], next, list, dir)
            #yukarı yoksa yönü sağa dön    
            else:
                fence+=1
                dir=0
                next=index+1
                if (x<xmax and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                #yukarı da yoksa geri aşağı dön
                else:
                    next=index+(xmax+1)
                    fence+=1
                    dir=1
                    fence+=Move(coordinates[next], next, list, dir)

    return fence
global firstindex
firstindex=0

i=0
for i in range(len(cachedir)):
    k=0
    for k in range(len(cache[i])):
        firstmove=True
        firstindex=cache[i][k][0]
        fenceno=Move(coordinates[firstindex],0,cache[i][k],0)
        print("Fence no..." , fenceno)





print("Result 1 is ..." , result1)