import re
f = open("./input/day13.txt", "r")
lines=f.readlines()
result1=0
result2=0

i=0
j=0

while i*4<len(lines):
    l1=lines[i*4].strip('\n')
    l2=lines[i*4+1].strip('\n')
    l3=lines[i*4+2].strip('\n')

    l1s=re.split(r"[:+, ]", l1)
    ax=int(l1s[4])
    ay=int(l1s[7])
    l2s=re.split(r"[:+, ]", l2)
    bx=int(l2s[4])
    by=int(l2s[7])
    l3s=re.split(r"[:+,= ]", l3)
    px=int(l3s[3])+10000000000000
    py=int(l3s[6])+10000000000000

    abutton=(px*by-py*bx)/(ax*by-bx*ay)
    bbutton=(py-(ay*abutton))/by

    if(abutton.is_integer() and bbutton.is_integer()):
        result1+=abutton*3+bbutton
    i+=1

print("Result 1 is .." , result1)
