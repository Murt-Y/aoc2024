f = open("./input/day16.txt", "r")
lines=f.readlines()

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

class Point:
    def __init__(self, x, y, val, dist):
        self.x=x
        self.y=y
        self.val=val
        self.dist=dist

def IndexCheck(x,y):
    return y*(xmax+1)+x

def PosCheck(index):
    xp=index%(xmax+1)
    yp=int((index-xp)/(xmax+1))
    return(xp,yp)

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

        temp=Point(xcount, ycount, c, float('inf'))

        cache.append([float('inf'),float('inf'),float('inf'),float('inf')])

        xcount+=1
        coordinates.append(temp)
    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1

def RotateR(dir):
    if(dir==0):
        return 1
    elif(dir==1):
        return 2
    elif (dir ==2):
        return 3
    else:
        return 0
def RotateL(dir):
    if(dir==0):
        return 3
    elif(dir==1):
        return 0
    elif (dir ==2):
        return 1
    else:
        return 2
def RotateF(dir):
    if(dir==0):
        return 2
    elif(dir==1):
        return 3
    elif (dir ==2):
        return 0
    else:
        return 1

def MoveRight(ind, score):
    x,y=PosCheck(ind)
    newindex=ind+1
    if(x+1<xmax and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and cache[newindex][0]>score):
        score+=1
        cache[newindex][0]=score
        p=[newindex, 0, score]
        return p
    else: 
        raise Exception
def MoveLeft(ind, score):
    x,y=PosCheck(ind)
    newindex=ind-1
    if(x>0 and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and cache[newindex][2]>score):
        score+=1
        cache[newindex][2]=score
        p=[newindex, 2, score]
        return p
    else: 
        raise Exception
def MoveUp(ind, score):
    x,y=PosCheck(ind)
    newindex=ind-(xmax+1)
    if(y>0 and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and cache[newindex][3]>score):
        score+=1
        cache[newindex][3]=score
        p=[newindex, 3, score]
        return p
    else: 
        raise Exception
def MoveDown(ind, score):
    x,y=PosCheck(ind)
    newindex=ind+(xmax+1)
    if(y<ymax and (coordinates[newindex].val=="." or coordinates[newindex].val=="E")  and cache[newindex][1]>score):
        score+=1
        cache[newindex][1]=score
        p=[newindex, 1, score]
        return p
    else: 
        raise Exception

def Step(index, dir, score):
    if(dir==0):
        return MoveRight(index, score)
    elif(dir==1):
        return MoveDown(index, score)
    elif (dir ==2):
        return MoveLeft(index, score)
    else:
        return MoveUp(index, score)

def CheckOp(activel):

    #printc()
    newl=[]
    for pointer in activel:
        try: 
            newp=Step (pointer[0], pointer[1], pointer[2])
            temp=newp.copy()
            newl.append(temp)
            dir=pointer[1]
            dirl=RotateL(dir)
            dirr=RotateR(dir)
            dirf=RotateF(dir)
            newindex=newp[0]
            newscore=newp[2]

            if(cache[newindex][dirl]>newscore+1000):
                newp[1]=dirl
                newp[2]=newscore+1000
                temp2=newp.copy()
                newl.append(temp2)
            if(cache[newindex][dirr]>newscore+1000):
                newp[1]=dirr
                newp[2]=newscore+1000
                temp2=newp.copy()
                newl.append(temp2)
            if(cache[newindex][dirf]>newscore+2000):
                newp[1]=dirf
                newp[2]=newscore+2000
                temp2=newp.copy()
                newl.append(temp2)
     

        except:
            continue
    activel=newl.copy()
    return activel



    # if coordinates[IndexCheck(x,y)].val=='E':
    #     coordinates[IndexCheck(x,y)].dist=score
    # else:
    #     Step(x,y,dir, score)
    #     dir=RotateL(dir)
    #     score+=1000
    #     Step(x,y,dir, score)
    #     dir=RotateF(dir)
    #     Step(x,y,dir, score)
    #     dir=RotateR(dir)
    #     score+=1000
    #     Step(x,y,dir, score)

def printc():
    k=0
    while(k<len(coordinates)):

            print(coordinates[k].val , end="")
            k+=1
            if(k%(xmax+1)==0):
                    print()

startindex=IndexCheck(cursorx, cursory)
cache[startindex][0]=0
p1=[startindex,0,0]
p2=[startindex,1,1000]
p3=[startindex,2,2000]
p4=[startindex,3,1000]
activel=[p1,p2,p3,p4]

l=len(activel)
while(l>0):
    l=CheckOp(activel)
    activel=l.copy()
    l=len(activel)

print(cache[IndexCheck(goalx,goaly)][0])
print(cache[IndexCheck(goalx,goaly)][1])
print(cache[IndexCheck(goalx,goaly)][2])
print(cache[IndexCheck(goalx,goaly)][3])
result1=min(cache[IndexCheck(goalx,goaly)])
print ("Result 1 is .....", result1)