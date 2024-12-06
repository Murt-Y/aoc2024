f = open("./input/day6.txt", "r")
safecount=0
lines=f.readlines()

class Point:
    def __init__(self, x, y, v):
        self.x=x
        self.y=y
        self.v=v

xcount=0
ycount=0
xmax=0
ymax=0
result=0
coordinates =[]

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

print (result)