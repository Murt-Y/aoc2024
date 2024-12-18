f = open("./input/day17.txt", "r")
lines=f.readlines()

reg_A=0
reg_B=0
reg_C=0
program=[]
result1=[]
result2=0

for l in lines:
    r=l.strip('\n')
    r=r.split(':')
    if r[0]=='Register A':
        reg_A=int(r[1])
    elif r[0]=='Register B':
        reg_B=int(r[1])
    elif r[0]=='Register C':
        reg_C=int(r[1])
    elif r[0]=='Program':
        p=r[1].split(',')
        for i in p:
            program.append(int(i))

def combo(op):
    mapping={
        0:0,
        1:1,
        2:2,
        3:3,
        4:reg_A,
        5:reg_B,
        6:reg_C

    }
    return mapping.get(op, "Invalid input")  # Default value for unmatched keys

def adv(num1, num2):
    #check truncate
    res=int(num1/num2)
    return res
def bxl(num1, num2):
    res=num1^num2
    return res
def bst(num2):
    #check truncate
    res=num2%8
    return res
def bxc(num1, num2):
    res=num1^num2
    return res
i=0
while(i<len(program)):
    opcode=program[i]
    opvalue=program[i+1]
    opcombo=combo(opvalue)

    if opcode==0:
        num2=2**opcombo
        reg_A=adv(reg_A,num2)
    if opcode==1:
        reg_B=bxl(reg_B,opvalue)
    if opcode==2:
        reg_B=bst(opcombo)
    if opcode==3:
        if(reg_A==0):
            pass
        else:
            i=opvalue
            continue
    if opcode==4:
        reg_B=bxc(reg_B,reg_C)
    if opcode==5:
        result1.append(bst(opcombo))
    if opcode==6:
        num2=2**opcombo
        reg_B=adv(reg_A,num2)
    if opcode==7:
        num2=2**opcombo
        reg_C=adv(reg_A,num2)
    i+=2

print(result1)