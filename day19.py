f = open("./input/day19.txt", "r")
lines=f.readlines()

towels=[]
reqs=[]
result1=0
result2=0

class pat:
    def __init__(self, pat, dest, quant):
        self.pat=pat
        self.dest=dest
        self.quant=quant

for i in range(len(lines)):
    if(i==0):
        towels=lines[i].split(',')
        towels=[item.strip() for item in towels]

    else:
        if(lines[i]=="\n"):
            continue
        reqs.append(lines[i].strip('\n'))

# for r in reqs:
#     activelist=[]
#     for t in towels:
#         length=len(t)
#         if(r[:length]==t):
#             activelist.append(t)


#     searchmode=True
#     while(searchmode==True and len(activelist)>0):
#         templist=[]
#         for a in activelist:
#             for t in towels:
#                 temp=(a+t).replace(" ", "")
#                 length=len(temp)
#                 if(r[:length]==temp and temp not in templist):
#                     templist.append(temp)
#                     if(temp==r and searchmode==True):
#                         result1+=1
#                         searchmode=False
        
#         activelist=templist.copy()

# print("The result for pt 1 is: ", result1)



for r in reqs:
    activelist=[]
    templist=[]
    processed=[]
    cache=[]
    for t in towels:
        length=len(t)
        if(r[:length]==t):
            p=pat(t,[],1)
            activelist.append(p)

    def find_pat(patt):
        return next((pat for pat in activelist if pat.pat == patt), None)


    def Move(p, c):
        dest=p.dest
        if len(dest)>0:
            p.quant=0
            for d in dest:
                point=find_pat(d)
                if (point==None):
                    activelist.append(pat(d, [], c))
                else:
                    Move(point, c)
        else:
            p.quant+=c



    for p in activelist:
        for t in towels:
            a=p.pat
            temp=(a+t).replace(" ", "")
            length=len(temp)
            if(r[:length]==temp):
                p.dest.append(temp)
        if(p.pat!=r):
            Move(p,p.quant)

            

    point=find_pat(r)
    if (point==None):
        pass
    else:
        result2+=point.quant


print("The result for pt 2 is: ", result2)