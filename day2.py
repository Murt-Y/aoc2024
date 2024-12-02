f = open("input/day2.txt", "r")
safecount=0
lines=f.readlines()

for x in lines:
    numbers = list(map(int, x.split()))
    c=len(numbers)
    i=1
    asc=True
    safe=True
    if(numbers[1]<numbers[0]):
        asc=False
    while (i<c):
        if(asc==True):
            if(numbers[i]>numbers[i-1]):
                if(numbers[i]-numbers[i-1] > 3):
                    safe=False
                    break
            else:
                safe=False
                break       
        else:
            if(numbers[i]<numbers[i-1]):
                if(numbers[i-1]-numbers[i] > 3):
                    safe=False
                    break
            else:
                safe=False
                break
        i+=1
    if(safe==True):
        safecount+=1           
print("Part 1 is ......" ,safecount)

def check_safe(nums):
    c=len(nums)
    i=1
    asc=True
    safe=True
    if(nums[1]<nums[0]):
        asc=False
    while (i<c):
        if(asc==True):
            if(nums[i]>nums[i-1]):
                if(nums[i]-nums[i-1] > 3):
                    return False
            else:
                return False    
        else:
            if(nums[i]<nums[i-1]):
                if(nums[i-1]-nums[i] > 3):
                    return False
            else:
                return False
        i+=1
    if(safe==True):
        return True         
    
safecount=0
for x in lines:
    numbers = list(map(int, x.split()))
    if(check_safe(numbers)==True):
        safecount+=1
    else:
        c=len(numbers)
        i=0
        while(i<c):
            tempnum=numbers.copy()
            tempnum.pop(i)
            if(check_safe(tempnum)==True):
                safecount+=1
                break
            i+=1

    
print("Part 2 is ......" ,safecount)