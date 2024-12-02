f = open("input/day1.txt", "r")
diff=0
nums1=[]
nums2=[]
for x in f:
    numbers = list(map(int, x.split()))
    nums1.append(numbers[0])
    nums2.append(numbers[1])
nums1.sort()
nums2.sort()
i=0
while (i<len(nums2)):
    diff+=abs(nums1[i]-nums2[i])
    i+=1
print("Part 1 is :   " , diff)

diff=0

for x in nums1:
    check=False
    eqcount=0
    for y in nums2:
        if(x==y):
            eqcount+=1
            check=True
        elif(check==True):
            break
    diff +=(eqcount*x)
print("Part 2 is :   " , diff)