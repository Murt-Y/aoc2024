import copy
import array
f = open("./input/day8.txt", "r")
lines=f.readlines()

xcount=0
ycount=0
xmax=0
ymax=0
result=0
result2=0
coordinates =[]




class Point:
    def __init__(self, x, y, val):
        self.x=x
        self.y=y
        self.val=val


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


uniqueletters=[]
pointbank=[]

count=0
for c in coordinates:
    if c.val=='.':
        count+=1
        continue
    else:
        temp=c.val
        try:
            i=uniqueletters.index(temp)
            pointbank[i].append(count)
        except:
            uniqueletters.append(temp)
            tlist=[]
            pointbank.append(tlist)
            i=len(uniqueletters)-1
            pointbank[i].append(count)

        count+=1

l=len(pointbank)
i=0
while(i<l):
    lz=len(pointbank[i])
    j=0
    while(j<lz):
        k=1
        while(j+k<lz):
            p1=coordinates[pointbank[i][j]]
            p2=coordinates[pointbank[i][j+k]]

            x1=p1.x+(p1.x-p2.x)
            y1=p1.y+(p1.y-p2.y)
            x2=p2.x+(p2.x-p1.x)
            y2=p2.y+(p2.y-p1.y)

            if (x1>xmax or y1>ymax or x1<0 or y1<0):
                pass
            else:
                coordinates[CheckIndex(x1,y1)].val='#'
            if (x2>xmax or y2>ymax or x2<0 or y2<0):
                pass
            else:
                coordinates[CheckIndex(x2,y2)].val='#'

            k+=1

        j+=1


    i+=1

result=0
for c in coordinates:
    if (c.val=='#'):
        result+=1

print("Part 1 is ......" ,result)



l=len(pointbank)
i=0
while(i<l):
    lz=len(pointbank[i])
    j=0
    while(j<lz):
        k=1
        while(j+k<lz):
            p1=coordinates[pointbank[i][j]]
            p2=coordinates[pointbank[i][j+k]]

            
            x1d=(p1.x-p2.x)
            y1d=(p1.y-p2.y)
            x2d=(p2.x-p1.x)
            y2d=(p2.y-p1.y)

            x1=p1.x+x1d
            y1=p1.y+y1d
            x2=p2.x+x2d 
            y2=p2.y+y2d

            while((x1>=0 and x1<=xmax) and (y1>=0 and y1<=ymax)):
                coordinates[CheckIndex(x1,y1)].val='#'
                x1+=x1d
                y1+=y1d

            while((x2>=0 and x2<=xmax) and (y2>=0 and y2<=ymax)):
                coordinates[CheckIndex(x2,y2)].val='#'
                x2+=x2d 
                y2+=y2d

            k+=1

        j+=1


    i+=1


result2=0
for c in coordinates:
    if (c.val!='.'):
        result2+=1

print("Part 2 is ......" ,result2)