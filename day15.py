f = open("./input/day15.txt", "r")
lines=f.readlines()

xcount=0
ycount=0
xmax=0
ymax=0
global robotx
global roboty
robotx=0
roboty=0
result1=0
result2=0
coordinates =[]
class Point:
    def __init__(self, x, y, val):
        self.x=x
        self.y=y
        self.val=val

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
        temp=Point(xcount, ycount, c)
        if(c=='@'):
            robotx=xcount
            roboty=ycount
        xcount+=1
        coordinates.append(temp)
    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1

i=ymax+2
instructions=''
while(i<len(lines)):
    instructions+=lines[i].strip("\n")
    i+=1

def PushLeft(index):
    empty=0
    global roboty, robotx
    if(coordinates[index].val=='@'):
        empty+=PushLeft(index-1)
        newindex=index-empty
        coordinates[index].val='.'
        coordinates[newindex].val='@'
        t=PosCheck(newindex)
        robotx=t[0]
        roboty=t[1]
    elif(coordinates[index].val=='.'):
        empty+=1
        empty+=PushLeft(index-1)
    elif(coordinates[index].val=='O'):
        empty+=PushLeft(index-1)
        newindex=index-empty
        coordinates[index].val='.'
        coordinates[newindex].val='O'
    elif(coordinates[index].val=='#'):
        return 0
    return empty

def PushRight(index):
    empty=0
    global roboty, robotx
    if(coordinates[index].val=='@'):
        empty+=PushRight(index+1)
        newindex=index+empty
        coordinates[index].val='.'
        coordinates[newindex].val='@'
        t=PosCheck(newindex)
        robotx=t[0]
        roboty=t[1]
    elif(coordinates[index].val=='.'):
        empty+=1
        empty+=PushRight(index+1)
    elif(coordinates[index].val=='O'):
        empty+=PushRight(index+1)
        newindex=index+empty
        coordinates[index].val='.'
        coordinates[newindex].val='O'
    elif(coordinates[index].val=='#'):
        return 0
    return empty

def PushUp(index):
    empty=0
    global roboty, robotx    
    if(coordinates[index].val=='@'):
        empty+=PushUp(index-(xmax+1))
        newindex=index-empty*(xmax+1)
        coordinates[index].val='.'
        coordinates[newindex].val='@'
        t=PosCheck(newindex)
        robotx=t[0]
        roboty=t[1]
    elif(coordinates[index].val=='.'):
        empty+=1
        empty+=PushUp(index-(xmax+1))
    elif(coordinates[index].val=='O'):
        empty+=PushUp(index-(xmax+1))
        newindex=index-empty*(xmax+1)
        coordinates[index].val='.'
        coordinates[newindex].val='O'
    elif(coordinates[index].val=='#'):
        return 0
    return empty

def PushDown(index):
    empty=0
    global roboty, robotx
    if(coordinates[index].val=='@'):
        empty+=PushDown(index+(xmax+1))
        newindex=index+empty*(xmax+1)
        coordinates[index].val='.'
        coordinates[newindex].val='@'
        t=PosCheck(newindex)
        robotx=t[0]
        roboty=t[1]
    elif(coordinates[index].val=='.'):
        empty+=1
        empty+=PushDown(index+(xmax+1))
    elif(coordinates[index].val=='O'):
        empty+=PushDown(index+(xmax+1))
        newindex=index+empty*(xmax+1)
        coordinates[index].val='.'
        coordinates[newindex].val='O'
    elif(coordinates[index].val=='#'):
        return 0
    return empty

startindex=IndexCheck(robotx,roboty)
def printc():
    k=0
    while(k<len(coordinates)):
            print(coordinates[k].val , end="")
            k+=1
            if(k%(xmax+1)==0):
                    print()

printc()

for c in instructions:
    robotindex=IndexCheck(robotx,roboty)
    if(c=='^'):
        PushUp(robotindex)
    elif(c=='v'):
        PushDown(robotindex)
    elif(c=='<'):
        PushLeft(robotindex)
    elif(c=='>'):
        PushRight(robotindex)
    print(c)
    printc()




printc()

print("Result for part 1 is ....", result1)
