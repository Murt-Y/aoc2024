import re


f = open("./input/day14.txt", "r")
lines=f.readlines()
result1=0
result2=0

xmax=101
ymax=103

robotpos=[]
robotv=[]

for l in lines:
    r=l.strip('\n')
    rs=re.split(r"[=, ]", r)
    rpos=[int(rs[1]),int(rs[2])]
    rv=[int(rs[4]),int(rs[5])]

    robotpos.append(rpos)
    robotv.append(rv)




def TimeS():

    for i in range(len(robotpos)):
        x=robotpos[i][0]
        y=robotpos[i][1]
        
        x=x+robotv[i][0]
        if x>=xmax:
            x=x-xmax
        elif x<0:
            x=x+xmax
        y=y+robotv[i][1]
        if y>=ymax:
            y=y-ymax
        elif y<0:
            y=y+ymax
        robotpos[i][0]=x
        robotpos[i][1]=y


for i in range(7677):
    TimeS()

tx=7677
for i in range(10):
    grid=['.']*xmax*ymax
    TimeS()
    for p in robotpos:
        gridno=p[0]+xmax*p[1]
        grid[gridno]='*'

    k=0
    consec=0
    printnow=True
    while(k<len(grid)):
        printv='.'
        if(grid[k]=='*'):
            consec+=1
            printv='*'
        k+=1
        print(printv , end="")
        if(k==len(grid)):
                break
        if(k%(xmax)==0):
                print()

    print('\n\n', "Times .................  ", i+tx+1 , "  ...................")

q1=0
q2=0
q3=0
q4=0


for p in robotpos:
    x='Q'
    y='Q'
    if(p[0] < (xmax-1)/2):
        x='L'
    elif(p[0] > (xmax-1)/2):
        x='R'
    if(p[1] < (ymax-1)/2):
        y='U'
    elif(p[1] > (ymax-1)/2):
        y='B'
    if(x=='L' and y=='U'):
        q1+=1
    elif(x=='R' and y=='U'):
        q2+=1
    elif(x=='L' and y=='B'):
        q3+=1
    elif(x=='R' and y=='B'):
        q4+=1

result1=q1*q2*q3*q4

print("Result for part 1 is ....", result1)

