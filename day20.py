f = open("./input/day20.txt", "r")
lines=f.readlines()
global xcount,ycount,xma,ymax
xcount=0
ycount=0
xmax=0
ymax=0
global cursorx ,cursory, goalx, goaly,cursordir
cursorx=0
cursory=0
cursordir=0
goalx=0
goaly=0
result1=0
result2=0
coordinates =[]
cache=[]
endlist=[]

class Point:
    def __init__(self, x, y, val, dist,hist):
        self.x=x
        self.y=y
        self.val=val
        self.dist=dist
        self.hist=hist

def IndexCheck(x,y):
    return y*(xmax+1)+x

def PosCheck(index):
    xp=index%(xmax+1)
    yp=int((index-xp)/(xmax+1))
    return(xp,yp)

def printc():
    k=0
    while(k<len(coordinates)):
            if(coordinates[k].dist<float("inf")):
                print('*', end="")
            else:
                print(coordinates[k].val , end="")
            k+=1
            if(k%(xmax+1)==0):
                    print()

for l in lines:
    if (l=='\n'):
        break
    for c in l:
        if(c=='\n'):
            break
        if(c=='S'):
            cursorx=xcount
            cursory=ycount
        if(c=='E'):
            goalx=xcount
            goaly=ycount

        temp=Point(xcount, ycount, c, float('inf'),[])

        xcount+=1
        coordinates.append(temp)
    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1

goalindex=IndexCheck(goalx, goaly)


def MoveLeft(p):
    x=p.x
    y=p.y
    h=p.hist
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind-1
    # if newindex==goalindex:
    #     print("here")
    if(x>0 and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        h.append(newindex)
        coordinates[newindex].hist=h
        return coordinates[newindex]
    else: 
        raise Exception


def MoveRight(p):
    x=p.x
    y=p.y
    h=p.hist
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind+1
    # if newindex==goalindex:
    #     print("here")
    if(x<xmax and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        h.append(newindex)
        coordinates[newindex].hist=h
        return coordinates[newindex]
    else: 
        raise Exception


def MoveDown(p):
    x=p.x
    y=p.y
    h=p.hist
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind+(xmax+1)
    # if newindex==goalindex:
    #     print("here")
    if(y<ymax and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        h.append(newindex)
        coordinates[newindex].hist=h
        return coordinates[newindex]
    else: 
        raise Exception

def MoveUp(p):
    x=p.x
    y=p.y
    h=p.hist
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind-(xmax+1)
    # if newindex==goalindex:
    #     print("here")
    if(y>0 and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        h.append(newindex)
        coordinates[newindex].hist=h
        return coordinates[newindex]
    else: 
        raise Exception

def Step(index, dir, score):
        return MoveRight(index, score)
        return MoveDown(index, score)

def Maze():
    startindex=IndexCheck(cursorx,cursory)
    coordinates[startindex].dist=0
    coordinates[startindex].hist.append(startindex)
    startpoint=coordinates[startindex]
    activelist=[]
    activelist.append(startpoint)
    while(len(activelist)>0):
        newlist=[]
        for ptocheck in activelist:
            try:
                t1=MoveRight(ptocheck)
                newlist.append(t1)
            except:
                pass
            
            try:
                t1=MoveDown(ptocheck)
                newlist.append(t1)
            except:
                pass
            
            try:
                t1=MoveLeft(ptocheck)
                newlist.append(t1)
            except:
                pass
            
            try:
                t1=MoveUp(ptocheck)
                newlist.append(t1)
            except:
                pass
        #printc()
        activelist=newlist.copy()

Maze()
result1=coordinates[goalindex].dist


def Reset():
    global xcount
    global ycount
    xcount=0
    ycount=0
    for l in lines:
        if (l=='\n'):
            break
        for c in l:
            if(c=='\n'):
                break
            if(c=='S'):
                cursorx=xcount
                cursory=ycount
            if(c=='E'):
                goalx=xcount
                goaly=ycount

            temp=Point(xcount, ycount, c, float('inf'),[])

            xcount+=1
            coordinates.append(temp)
        xmax=xcount-1
        xcount=0
        ycount+=1
    ymax=ycount-1
result2=0
change=True

for i in range(len(coordinates)):
    if change== True:
        coordinates=[]
        Reset()

    if coordinates[i].val=='#':
        change=True
        coordinates[i].val='.'
        Maze()
        res2=coordinates[goalindex].dist
        save=result1-res2
        if save>=100:
            result2+=1
    else:
        change=False


print ("Result 1 is .....", result1)
print ("Result 2 is .....", result2)