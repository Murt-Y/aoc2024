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
robot2x=0
robot2y=0
result1=0
result2=0
coordinates =[]
coordinates2=[]
class Point:
    def __init__(self, x, y, val):
        self.x=x
        self.y=y
        self.val=val

def IndexCheck(x,y):
    return y*(xmax+1)+x
def IndexCheck2(x,y):
    return y*(xmax2+1)+x
def PosCheck(index):
    xp=index%(xmax+1)
    yp=int((index-xp)/(xmax+1))
    return(xp,yp)
def PosCheck2(index):
    xp=index%(xmax2+1)
    yp=int((index-xp)/(xmax2+1))
    return(xp,yp)

for l in lines:
    if (l=='\n'):
        break
    for c in l:
        if(c=='\n'):
            break
        elif(c=='O'):
            c2='[]'
        elif(c=='.'):
            c2='..'
        elif(c=='#'):
            c2='##'
        if(c=='@'):
            c2='@.'
            robotx=xcount
            roboty=ycount
            robot2x=xcount*2
            robot2y=ycount

        temp=Point(xcount, ycount, c)
        temp21=Point(xcount*2, ycount, c2[0])
        temp22=Point(xcount*2+1, ycount, c2[1])

        xcount+=1
        coordinates.append(temp)
        coordinates2.append(temp21)
        coordinates2.append(temp22)

    xmax=xcount-1
    xcount=0
    ycount+=1
ymax=ycount-1
xmax2=xmax*2+1

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
        #empty+=PushLeft(index-1)
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
        #empty+=PushRight(index+1)
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
        #empty+=PushUp(index-(xmax+1))
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
        #empty+=PushDown(index+(xmax+1))
    elif(coordinates[index].val=='O'):
        empty+=PushDown(index+(xmax+1))
        newindex=index+empty*(xmax+1)
        coordinates[index].val='.'
        coordinates[newindex].val='O'
    elif(coordinates[index].val=='#'):
        return 0
    return empty

def PushLeft2(index):
    empty=False
    global robot2y, robot2x
    if(coordinates2[index].val=='@'):
        empty=PushLeft2(index-1)
        if empty==True:
            newindex=index-1
            coordinates2[index].val='.'
            coordinates2[newindex].val='@'
            t=PosCheck2(newindex)
            robot2x=t[0]
            robot2y=t[1]
    elif(coordinates2[index].val=='.'):
        empty=True
    elif(coordinates2[index].val=='[' or coordinates2[index].val==']'):
        empty=False
        empty=PushLeft2(index-1)
        if empty==True:
            v=coordinates2[index].val
            newindex=index-1
            coordinates2[index].val='.'
            coordinates2[newindex].val=v
    elif(coordinates2[index].val=='#'):
        return False
    return empty

def PushRight2(index):
    empty=False
    global robot2y, robot2x
    if(coordinates2[index].val=='@'):
        empty=PushRight2(index+1)
        if empty==True:
            newindex=index+1
            coordinates2[index].val='.'
            coordinates2[newindex].val='@'
            t=PosCheck2(newindex)
            robot2x=t[0]
            robot2y=t[1]
    elif(coordinates2[index].val=='.'):
        empty=True
    elif(coordinates2[index].val=='[' or coordinates2[index].val==']'):
        empty=False
        empty=PushRight2(index+1)
        if empty==True:
            v=coordinates2[index].val
            newindex=index+1
            coordinates2[index].val='.'
            coordinates2[newindex].val=v
    elif(coordinates2[index].val=='#'):
        return False
    return empty

def PushUp2(index):
    empty=False
    global robot2y, robot2x
    if(coordinates2[index].val=='@'):
        empty=PushUp2(index-(xmax2+1))
        if empty==True:
            newindex=index-(xmax2+1)
            coordinates2[index].val='.'
            coordinates2[newindex].val='@'
            t=PosCheck2(newindex)
            robot2x=t[0]
            robot2y=t[1]
    elif(coordinates2[index].val=='.'):
        empty=True
        #empty+=PushUp(index-(xmax+1))
    elif(coordinates2[index].val=='['):
        empty=PushUp2(index-(xmax2+1))and PushUp2(index-(xmax2+1)+1)
        if empty==True:
            newindex=index-(xmax2+1)
            newindex2=index-(xmax2+1)+1
            coordinates2[index].val='.'
            coordinates2[index+1].val='.'
            coordinates2[newindex].val='['
            coordinates2[newindex2].val=']'
    elif(coordinates2[index].val==']'):
        empty=PushUp2(index-(xmax2+1))and PushUp2(index-(xmax2+1)-1)
        if empty==True:
            newindex=index-(xmax2+1)
            newindex2=index-(xmax2+1)-1
            coordinates2[index].val='.'
            coordinates2[index-1].val='.'
            coordinates2[newindex].val=']'
            coordinates2[newindex2].val='['
    elif(coordinates2[index].val=='#'):
        return False
    return empty

def PushDown2(index):
    empty=False
    global robot2y, robot2x   
    if(coordinates2[index].val=='@'):
        empty=PushDown2(index+(xmax2+1))
        if empty==True:
            newindex=index+(xmax2+1)
            coordinates2[index].val='.'
            coordinates2[newindex].val='@'
            t=PosCheck2(newindex)
            robot2x=t[0]
            robot2y=t[1]
    elif(coordinates2[index].val=='.'):
        empty=True
        #empty+=PushUp(index-(xmax+1))
    elif(coordinates2[index].val=='['):
        empty=PushDown2(index+(xmax2+1))and PushDown2(index+(xmax2+1)+1)
        if empty==True:
            newindex=index+(xmax2+1)
            newindex2=index+(xmax2+1)+1
            coordinates2[index].val='.'
            coordinates2[index+1].val='.'
            coordinates2[newindex].val='['
            coordinates2[newindex2].val=']'
    elif(coordinates2[index].val==']'):
        empty=PushDown2(index+(xmax2+1))and PushDown2(index+(xmax2+1)-1)
        if empty==True:
            newindex=index+(xmax2+1)
            newindex2=index+(xmax2+1)-1
            coordinates2[index].val='.'
            coordinates2[index-1].val='.'
            coordinates2[newindex].val=']'
            coordinates2[newindex2].val='['
    elif(coordinates2[index].val=='#'):
        return False
    return empty


startindex=IndexCheck(robotx,roboty)
startindex2=IndexCheck2(robot2x,robot2y)

def printc():
    k=0
    while(k<len(coordinates)):
            print(coordinates[k].val , end="")
            k+=1
            if(k%(xmax+1)==0):
                    print()
def printc2():
    k=0
    while(k<len(coordinates2)):
            print(coordinates2[k].val , end="")
            k+=1
            if(k%(xmax2+1)==0):
                    print()
printc2()

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

for c in instructions:
    robotindex=IndexCheck2(robot2x,robot2y)
    if(c=='^'):
        PushUp2(robotindex)
    elif(c=='v'):
        PushDown2(robotindex)
    elif(c=='<'):
        PushLeft2(robotindex)
    elif(c=='>'):
        PushRight2(robotindex)
        



printc2()




for c in coordinates:
    if(c.val=='O'):
        result1+=(c.y)*100+c.x
for m in coordinates2:
    if(m.val=='['):
        result2+=(m.y)*100+m.x


print("Result for part 1 is ....", result1)
print("Result for part 2 is ....", result2)
