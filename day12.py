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

global firstindex
global firstmove


def Move(p, index, list, dir):
    global firstindex
    global firstmove
    fence=0
    
    x=p.x
    y=p.y
    next=0

    if index==firstindex:
        if firstmove==False:
            fence+=1
            firstmove=True
        else:
            finish=False
            if dir==1:
                next=index+1
                if not (x<xmax and next in list):
                    fence+=2
                    finish=True
            elif dir==2:
                next=index+(xmax+1)
                if not (y<ymax and next in list):
                    fence+=1
                    finish=True
            elif dir==3:
                next=index-1
                if not (x>0 and next in list):
                    fence+=0
                    finish=True 
            if finish==True:    
                return fence


    if(dir==0):
        #sağa doğru geldiyse önce yukarı bak varsa yönü yukarı dön yukarı git
        next=index-(xmax+1)
        if(y>0 and next in list):
            fence+=1
            dir=3
            fence+= Move(coordinates[next], next, list, dir)
            return fence
        #yukari yoksa saga bak sagda varsa ona gec fence artmiyor
        else:
            next=index+1
            if(x<xmax and next in list):
                fence+=Move(coordinates[next], next, list, dir)
                return fence
            #yan yoksa yönü aşağıya dön    
            else:
                fence+=1
                dir=1
                next=index+xmax+1
                if (y<ymax and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                    return fence
                #aşağı da yoksa geri sola dön
                else:
                    next=index-1
                    fence+=1
                    dir=2
                    if(x>0 and next in list):
                        fence+=Move(coordinates[next], next, list, dir)
                        return fence
                    else:
                        fence+=1
                        return fence
                    
    elif(dir==1):
        #aşağıya doğru geldiyse önce sağa bak varsa yönü sağa dön sağa git
        next=index+1
        if(x<xmax and next in list):
            fence+=1
            dir=0
            fence+= Move(coordinates[next], next, list, dir)
            return fence
        #sağ yoksa aşağıya varsa ona gec fence artmiyor
        else:
            next=index+xmax+1
            if(y<ymax and next in list):
                fence+=Move(coordinates[next], next, list, dir)
                return fence
            #aşağı yoksa yönü sola dön    
            else:
                fence+=1
                dir=2
                next=index-1
                if (x>0 and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                    return fence
                #sol da yoksa geri yukarı dön
                else:
                    next=index-(xmax+1)
                    fence+=1
                    dir=3
                    if(y>0 and next in list):
                        fence+=Move(coordinates[next], next, list, dir)
                        return fence
                    else:
                        fence+=1
                        return fence
    if(dir==2):
        #sola doğru geldiyse önce aşağıya bak varsa yönü aşağı dön aşağı git
        next=index+(xmax+1)
        if(y<ymax and next in list):
            fence+=1
            dir=1
            fence+= Move(coordinates[next], next, list, dir)
            return fence
        #aşağı yoksa sola bak solda varsa ona gec fence artmiyor
        else:
            next=index-1
            if(x>0 and next in list):
                fence+=Move(coordinates[next], next, list, dir)
                return fence
            #yan yoksa yönü yukar dön    
            else:
                fence+=1
                dir=3
                next=index-(xmax+1)
                if (y>0 and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                    return fence
                #yukarı da yoksa geri sağa dön
                else:
                    next=index+1
                    fence+=1
                    dir=0
                    if(x<xmax and next in list):
                        fence+=Move(coordinates[next], next, list, dir)
                        return fence
                    else:
                        fence+=1
                        return fence
    elif(dir==3):
        #yukar doğru geldiyse önce sola bak varsa yönü sola dön sola git
        next=index-1
        if(x>0 and next in list):
            fence+=1
            dir=2
            fence+= Move(coordinates[next], next, list, dir)
            return fence
        #sol yoksa yukar varsa ona gec fence artmiyor
        else:
            next=index-(xmax+1)
            if(y>0 and next in list):
                fence+=Move(coordinates[next], next, list, dir)
                return fence
            #yukarı yoksa yönü sağa dön    
            else:
                fence+=1
                dir=0
                next=index+1
                if (x<xmax and next in list):
                    fence+=Move(coordinates[next], next, list, dir)
                    return fence
                #yukarı da yoksa geri aşağı dön
                else:
                    next=index+(xmax+1)
                    fence+=1
                    dir=1
                    if(y<ymax and next in list):
                        fence+=Move(coordinates[next], next, list, dir)
                        return fence
                    else:
                        fence+=1
                        return fence

    return fence


i=0
for i in range(len(cachedir)):
    k=0
    for k in range(len(cache[i])):
        firstindex=cache[i][k][0]
        firstmove=False
        nofence=(Move(coordinates[firstindex],firstindex,cache[i][k],0))
        arearegion=len(cache[i][k])
        result2+=(nofence*arearegion)





print("Result 1 is ..." , result1)
print("Result 2 is ..." , result2)