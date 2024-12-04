f = open("input/day4.txt", "r")
safecount=0
lines=f.readlines()

class Point:
    def __init__(self, x, y, v):
        self.x=x
        self.y=y
        self.v=v

coordinates =[]
xcount=0
ycount=0
xmax=0
ymax=0
result=0

def CheckIndex(xt, yt):
    return(yt*(xmax+1)+xt)

# def CheckUp(point, target):
#     if(point.y==0):
#         return
#     next=CheckIndex(point.x, point.y-1)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckUp(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckUp(coordinates[next],'A')
        
# def CheckDown(point, target):
#     if(point.y==ymax):
#         return
#     next=CheckIndex(point.x, point.y+1)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckDown(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckDown(coordinates[next],'A')
        
# def CheckRight(point, target):
#     if(point.x==xmax):
#         return
#     next=CheckIndex(point.x+1, point.y)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckRight(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckRight(coordinates[next],'A')

# def CheckLeft(point, target):
#     if(point.x==0):
#         return
#     next=CheckIndex(point.x-1, point.y)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckLeft(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckLeft(coordinates[next],'A')    
        
# def CheckUpLeft(point, target):
#     if(point.x==0 or point.y==0):
#         return
#     next=CheckIndex(point.x-1, point.y-1)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckUpLeft(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckUpLeft(coordinates[next],'A')   

# def CheckUpRight(point, target):
#     if(point.x==xmax or point.y==0):
#         return
#     next=CheckIndex(point.x+1, point.y-1)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckUpRight(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckUpRight(coordinates[next],'A')   

# def CheckDownLeft(point, target):
#     if(point.x==0 or point.y==ymax):
#         return
#     next=CheckIndex(point.x-1, point.y+1)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckDownLeft(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckDownLeft(coordinates[next],'A')   

# def CheckDownRight(point, target):
#     if(point.x==xmax or point.y==ymax):
#         return
#     next=CheckIndex(point.x+1, point.y+1)
#     if(coordinates[next].v==target):
#         if(target=='S'):
#             return True
#         elif(target=='A'):
#             return CheckDownRight(coordinates[next],'S')
#         elif(target=='M'):
#             return CheckDownRight(coordinates[next],'A')   

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
    if(coordinates[i].x%6==0):
        print()

# for c in coordinates:
#     if(c.v=='X'):
#         if(CheckUp(c, 'M')):
#             result+=1
#         if(CheckDown(c, 'M')):
#             result+=1
#         if(CheckLeft(c, 'M')):
#             result+=1
#         if(CheckRight(c, 'M')):
#             result+=1
#         if(CheckUpLeft(c, 'M')):
#             result+=1
#         if(CheckUpRight(c, 'M')):
#             result+=1
#         if(CheckDownLeft(c, 'M')):
#             result+=1
#         if(CheckDownRight(c, 'M')):
#             result+=1



# print("Part 1 is ......" ,result)



        


  
        
def CheckUpLeft(point):
    if(point.x==0 or point.y==0):
        return
    next=CheckIndex(point.x-1, point.y-1)
    return(coordinates[next].v)

def CheckUpRight(point):
    if(point.x==xmax or point.y==0):
        return
    next=CheckIndex(point.x+1, point.y-1)
    return(coordinates[next].v)

def CheckDownLeft(point):
    if(point.x==0 or point.y==ymax):
        return
    next=CheckIndex(point.x-1, point.y+1)
    return(coordinates[next].v) 

def CheckDownRight(point):
    if(point.x==xmax or point.y==ymax):
        return
    next=CheckIndex(point.x+1, point.y+1)
    return(coordinates[next].v)

for c in coordinates:
    if(c.v=='A'):
        if((CheckUpLeft(c)=='M' and CheckDownRight(c)=='S') or (CheckUpLeft(c)=='S' and CheckDownRight(c)=='M')):
            if((CheckUpRight(c)=='M' and CheckDownLeft(c)=='S') or (CheckUpRight(c)=='S' and CheckDownLeft(c)=='M')):
                result +=1

print (result)