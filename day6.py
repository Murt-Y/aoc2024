f = open("./input/day6.txt", "r")
safecount=0
lines=f.readlines()

class Point:
    def __init__(self, x, y, v):
        self.x=x
        self.y=y
        self.v=v

def Rotate():
    global user
    if(user[1]=='^'):
        user[1]='>'
    elif(user[1]=='>'):
        user[1]='v'
    elif(user[1]=='v'):
        user[1]='<'
    elif(user[1]=='<'):
        user[1]='^'

def Move(point):
    global user
    if(user[1]=='^'):
        MoveUp(point)
    elif(user[1]=='>'):
        MoveRight(point)
    elif(user[1]=='v'):
        MoveDown(point)
    elif(user[1]=='<'):
        MoveLeft(point)

def MoveUp(point):
    if(point.y==0):
        global userin
        userin=False
        return
    next=CheckIndex(point.x, point.y-1)
    if(coordinates[next].v=='#'):
        Rotate(point)
    else:
        point.v='X'
        coordinates[next].val='^'
        user[0]=next


xcount=0
ycount=0
xmax=0
ymax=0
result=0
coordinates =[]
user=[]

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
            return CheckIndex(c.x, c.y),c.v

user=UserLoc()

userin=True

while(userin==True):
    Move(coordinates[user[0]])
        
    

print (result)