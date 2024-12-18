f = open("./input/day18.txt", "r")
lines=f.readlines()

xcount=0
ycount=0
xmax=71
ymax=71
global cursorx ,cursory, goalx, goaly,cursordir
cursorx=0
cursory=0
cursordir=0
goalx=70
goaly=70
result1=0
result2=0
coordinates =[]
cache=[]
endlist=[]

class Point:
    def __init__(self, x, y, val, dist):
        self.x=x
        self.y=y
        self.val=val
        self.dist=dist

def IndexCheck(x,y):
    return y*(xmax)+x

def PosCheck(index):
    xp=index%(xmax)
    yp=int((index-xp)/(xmax))
    return(xp,yp)



for i in range(71*71):
        temp=Point(xcount, ycount, '.', float('inf'))
        coordinates.append(temp)
        xcount+=1
        if(xcount==xmax):
            xcount=0
            ycount+=1





for i in range(1024):

    l=lines[i].split(',')
    ind=IndexCheck(int(l[0]),int(l[1]))
    coordinates[ind].val='#'


def MoveLeft(p):
    x=p.x
    y=p.y
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind-1
    # if newindex==goalindex:
    #     print("here")
    if(x>0 and coordinates[newindex].val=="." and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        return coordinates[newindex]
    else: 
        raise Exception


def MoveRight(p):
    x=p.x
    y=p.y
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind+1
    # if newindex==goalindex:
    #     print("here")
    if(x<xmax and coordinates[newindex].val=="." and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        return coordinates[newindex]
    else: 
        raise Exception


def MoveDown(p):
    x=p.x
    y=p.y
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind+(xmax)
    # if newindex==goalindex:
    #     print("here")
    if(y<ymax and coordinates[newindex].val=="." and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        return coordinates[newindex]
    else: 
        raise Exception

def MoveUp(p):
    x=p.x
    y=p.y
    score=p.dist+1
    ind=IndexCheck(x,y)
    newindex=ind-(xmax)
    # if newindex==goalindex:
    #     print("here")
    if(y>0 and coordinates[newindex].val=="." and coordinates[newindex].dist>score):
        coordinates[newindex].dist=score
        return coordinates[newindex]
    else: 
        raise Exception

def Step(index, dir, score):
        return MoveRight(index, score)
        return MoveDown(index, score)

def Maze():
    coordinates[0].dist=0
    startpoint=coordinates[0]
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
        activelist=newlist.copy()

Maze()
result1=coordinates[-1].dist

search=True

i=1024

while search:
    for c in coordinates:
        c.dist=float('inf')
    l=lines[i].split(',')
    indtoadd=IndexCheck(int(l[0]),int(l[1]))
    coordinates[indtoadd].val='#'

    Maze()

    if(coordinates[-1].dist<float('inf')):
        pass
    else:
        result2=l
        search=False

    i+=1

print ("Result 1 is .....", result1)
print ("Result 2 is .....", result2)