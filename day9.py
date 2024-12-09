f = open("./input/day9.txt", "r")
diskmap=f.readlines()

result1=0
result2=0

id=0

disk=[]
diskhead=0
size=0

for d in diskmap[0]:
    size=int(d)
    if(diskhead==0):
        diskhead=1
        for x in range(size):
            disk.append(id)
        id+=1

    else:
        diskhead=0
        for x in range(size):
            disk.append('.')


c=0
for d in disk:
    if(d=='.'):
        temp='.'
        while(temp=='.'):
            temp=disk.pop()
        disk[c]=temp



    c+=1

c=0
for d in disk:
    result1+=(c*int(d))
    c+=1

print("Result of Pt 1 is .... " , result1)

diskhead=0
disk=[]
global revdisk
revdisk=[]
id=0
count=0

for d in diskmap[0]:
    disk.append(int(d))

i=0
l=len(disk)
id=0

while(i*2<l-1):
    revdisk.append(id)
    revdisk.append(disk[i*2])
    revdisk.append(disk[i*2+1])
    id+=1
    i+=1
revdisk.append(id)
revdisk.append(disk[i*2])
revdisk.append(0)

findisk=[]


def CheckSlot(s, id):
    checkcomplete=False
    k=0
    while(not checkcomplete):

        if(revdisk[k]==id):
            checkcomplete=True
            return False
        elif(revdisk[k+2]>=s):
            em=revdisk[k+2]
            revdisk[k+2]=0
            revdisk.insert(k+3,em-size)
            revdisk.insert(k+3, size)
            revdisk.insert(k+3,id)
            checkcomplete=True
            return True
 

        
        k+=3

l=len(revdisk)
i=l
while(i>0):
    size=revdisk[i-2]
    id=revdisk[i-3]
    if(CheckSlot(size, id)):
        i+=3
        totsize=revdisk[i-2]+revdisk[i-1]
        revdisk[i-2]=0
        revdisk[i-1]=totsize

    
    i-=3

i=0
while (i<len(revdisk)):
    id=revdisk[i]
    rep=revdisk[i+1]
    for t in range(rep):
        findisk.append(id)
    for t in range(revdisk[i+2]):
        findisk.append('.')
    i+=3

c=0
for d in findisk:
    if(d != '.'):
        result2+=(c*int(d))
    c+=1

print("Result of Pt 2 is .... " , result2)