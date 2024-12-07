import copy
import array
f = open("./input/day6.txt", "r")
safecount=0
lines=f.readlines()

xcount=0
ycount=0
xmax=0
ymax=0
result=0
coordinates =[]
user=[0,0]



class Point:
    def __init__(self, x, y, v):
        self.x=x
        self.y=y
        self.v=v



def Rotate():
    global user
    if(user[1]=='^'):
        memright[user[0]]=1
        user[1]='>'
    elif(user[1]=='>'):
        memdown[user[0]]=1
        user[1]='v'
    elif(user[1]=='v'):
        memleft[user[0]]=1
        user[1]='<'
    elif(user[1]=='<'):
        memup[user[0]]=1
        user[1]='^'

def Move(point):
    global user
    if(user[1]=='^'):
        memup[user[0]]=1
        MoveUp(point)
    elif(user[1]=='>'):
        memright[user[0]]=1
        MoveRight(point)
    elif(user[1]=='v'):
        memdown[user[0]]=1
        MoveDown(point)
    elif(user[1]=='<'):        
        memleft[user[0]]=1
        MoveLeft(point)

def MoveUp(point):
    global user
    if(point.y==0):
        global userin
        userin=False
        return
    next=user[0]-(xmax+1)
    if(memup[next]==1):
        global userloop
        userloop=True
    if(coordinates[next].v=='#'):
        Rotate()
    else:
        point.v='X'
        coordinates[next].val='^'
        user[0]=next

def MoveDown(point):
    global user
    if(point.y==ymax):
        global userin
        userin=False
        return
    next=user[0]+xmax+1
    if(memdown[next]==1):
        global userloop
        userloop=True
    if(coordinates[next].v=='#'):
        Rotate()
    else:
        point.v='X'
        coordinates[next].val='v'
        user[0]=next
        
def MoveRight(point):
    global user
    if(point.x==xmax):
        global userin
        userin=False
        return
    next=user[0]+1
    if(memright[next]==1):
        global userloop
        userloop=True
    if(coordinates[next].v=='#'):
        Rotate()
    else:
        point.v='X'
        coordinates[next].val='^'
        user[0]=next

def MoveLeft(point):
    global user
    if(point.x==0):
        global userin
        userin=False
        return
    next=user[0]-1
    if(memleft[next]==1):
        global userloop
        userloop=True
    if(coordinates[next].v=='#'):
        Rotate()
    else:
        point.v='X'
        coordinates[next].val='^'
        user[0]=next

def CheckIndex(xt, yt):
    return(yt*(xmax+1)+xt)

for t in lines:
    for c in t:
        if(c=='\n'):
            break
        temp=Point(xcount, ycount, c)
        xcount+=1
        coordinates.append(temp)
    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1

poscount=len(coordinates)
result2=0
memup = array.array('b', [0]*poscount)
memdown = array.array('b', [0]*poscount)
memright = array.array('b', [0]*poscount)
memleft = array.array('b', [0]*poscount)

initialpos=copy.deepcopy(coordinates)

def printgrid():
    i=0
    while(i<len(coordinates)):
        print(coordinates[i].v , end="")
        i+=1
        if(i==len(coordinates)):
            break
        if(coordinates[i].x%(xmax+1)==0):
            print()

def UserLoc():
        for c in coordinates:
            if (c.v == '^' or c.v=='>' or c.v=='<' or c.v=='v'):
                return [CheckIndex(c.x, c.y),c.v]

user=UserLoc()
inituser=user.copy()

userin=True
userloop=False



while(userin==True):
    Move(coordinates[user[0]])
#   printgrid()
#    print("\n")

if(userin==False):
    coordinates[user[0]].v='X'
    printgrid()
    print("\n")

for c in coordinates:
    if (c.v=='X'):
        result+=1
print ("Part 1 is ......" ,result)

trypos=copy.deepcopy(initialpos)


tryouts=0
while (tryouts<poscount):

    coordinates=copy.deepcopy(initialpos)
    user=inituser.copy()
    for i in range(poscount):
        memleft[i]=0
        memdown[i]=0
        memright[i]=0
        memup[i]=0
    coordinates[tryouts].v='#'
    userin=True
    userloop=False
    while(userin==True):
        Move(coordinates[user[0]])
        if (userin==True and userloop==True):
            result2+=1
            break
        #poslist.append(user[0])
        #historicpos.append(user.copy())
        #printgrid()
        #print("\n")

    tryouts+=1





print(result2)