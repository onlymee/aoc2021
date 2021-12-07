answer1=-1
answer2=-1

with open("day07/input.txt",'r') as input:
    lines=input.read().splitlines()


pos=[int(i) for i in lines[0].split(',')]

def S(n):
    return int(n*(n+1)/2)

minfuel=2**100
minfuel2=2**100
for h in range(min(pos),max(pos)+1):
    fuel=0
    fuel2=0
    for p in pos:
        fuel+=abs(p-h)
        fuel2+=S(abs(p-h))
    if fuel<minfuel:
        minfuel=fuel
    if fuel2<minfuel2:
        minfuel2=fuel2


answer1=minfuel
answer2=minfuel2
print(answer1,answer2)