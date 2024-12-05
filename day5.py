f = open("aoc2024/input/day5.txt", "r")
safecount=0
lines=f.readlines()
rules=[]
updates=[]
inputswitch=False
result=0
result2=0

for x in lines:
    if x=='\n':
        inputswitch=True
        continue
    if inputswitch==False:
        rules.append(x)
    else:
        updates.append(x)

i=0
for r in rules: 
    rules[i]=rules[i].split('|')
    rules[i][1]=rules[i][1].rstrip('\n')
    i+=1

def CheckRule(x,y):
    for r in rules:
        if (r[0]==y and r[1]==x):
            return False
    return True

for u in updates:
    u=u.rstrip('\n')
    i=0
    uopen = u.split(',')
    z=len(uopen)
    mid=(z-1)//2
    checkr=True
    while(i<z):
        k=1
        while(i+k<z):
            if(CheckRule(uopen[i],uopen[i+k])==False):
                checkr=False
                t=uopen[i]
                uopen[i]=uopen[i+k]
                uopen[i+k]=t
            k+=1
        i+=1
    if(checkr==True):
        result+=int(uopen[mid])
    if(checkr==False):
        result2+=int(uopen[mid])
print(result)
print(result2)