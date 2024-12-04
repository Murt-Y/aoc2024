import re
f = open("input/day3.txt", "r")

input=f.read()
regex=r'mul\(\d{1,3},\d{1,3}\)'
actions = re.findall(regex, input)
print(actions)
result=0

for x in actions:
    startifirst=re.search(r'\(' , x).start()
    startisecond=re.search(r'\,' , x).start()
    endisecond=re.search(r'\)' , x).start()

    first=int(x[startifirst+1:startisecond])
    second=int(x[startisecond+1:endisecond])
    result+=(first*second)

print("Part 1 is ......" ,result)

regex=r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
actions = re.findall(regex, input)
print(actions)
result=0

multiplier=1
for x in actions:
    if(x=="do()"):
        multiplier=1
    elif(x=="don't()"):
        multiplier=0
    else:
        startifirst=re.search(r'\(' , x).start()
        startisecond=re.search(r'\,' , x).start()
        endisecond=re.search(r'\)' , x).start()

        first=int(x[startifirst+1:startisecond])
        second=int(x[startisecond+1:endisecond])
        result+=(first*second*multiplier)
print("Part 2 is ......" ,result)