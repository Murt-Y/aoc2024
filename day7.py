f = open("input/day7.txt", "r")
lines=f.readlines()
global result
result=0
global result2
result2=0

def CheckSum(a,b):
    return a+b

def CheckMul(a,b):
    return a*b

def CheckCon(a,b):
    a=str(a)
    b=str(b)
    a=b+a
    return int(a)

def CheckOp(nums, sum):
    global target, result
    c1=int(nums[0].strip("\n"))
    #first check the sum 
    r1=CheckSum(c1,sum)
    #if reached the target and no more numbers left to check return true
    if(r1==target and len(nums)==1):
        return True
    #if it didn't pass the target and there are numbers to go take the sum and go again
    if(r1 <= target):
        if(len(nums)>1):
            if(CheckOp(nums[1:], r1)):
                return True
    #if taking the sum doesn't work check mult.
    r1=CheckMul(c1, sum)

    if(r1==target and len(nums)==1):
        return True
    #if it didn't pass the target and there are numbers to go take the mult. and go again
    if(r1 <= target):
        if(len(nums)>1):
            if(CheckOp(nums[1:], r1)):
                return True
       
def CheckOp2(nums, sum):
    global target, result
    c1=int(nums[0].strip("\n"))

    #first check the sum 
    r1=CheckSum(c1,sum)
    #if reached the target and no more numbers left to check return true
    if(r1==target and len(nums)==1):
        return True
    #if it didn't pass the target and there are numbers to go take the sum and go again
    if(r1 <= target):
        if(len(nums)>1):
            if(CheckOp2(nums[1:], r1)):
                return True
    #if taking the sum doesn't work check mult.
    r1=CheckMul(c1, sum)
    if(r1==target and len(nums)==1):
        return True
    #if it didn't pass the target and there are numbers to go take the mult. and go again
    if(r1 <= target):
        if(len(nums)>1):
            if(CheckOp2(nums[1:], r1)):
                return True
    r1=CheckCon(c1, sum)
    if(r1==target and len(nums)==1):
        return True
    #if it didn't pass the target and there are numbers to go take the mult. and go again
    if(r1 <= target):
        if(len(nums)>1):
            if(CheckOp2(nums[1:], r1)):
                return True


global target

def CheckLine(line):
    global target,result
    code = line.split(" ")
    target=int(code[0][:-1])
    #take the first number and sends the rest to process
    sum=int(code[1])
    nums=code[2:]
    if(CheckOp(nums, sum)):
        result+=target

def CheckLine2(line):
    global target,result,result2
    code = line.split(" ")
    target=int(code[0][:-1])
    #take the first number and sends the rest to process
    sum=int(code[1])
    nums=code[2:]
    if(CheckOp2(nums, sum)):
        result2+=target

for t in lines:
    CheckLine(t)


for t in lines:
    CheckLine2(t)





print("Result for part 1 is .... " , result)
print("Result for part 2 is .... " , result2)
