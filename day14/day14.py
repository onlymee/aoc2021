from collections import defaultdict
answer1=-1
answer2=-1

with open("day14/input.txt",'r') as input:
    lines=input.read().splitlines()


start=lines[0]
ins={}
inpairs={}
for line in lines[2:]:
    fr,to = line.split(' -> ')
    ins[fr]=to
    inpairs[fr]=[fr[0]+to,to+fr[1]]

pol=start
print(start)
for s in range(10):
    newpol=pol[0]
    for i in range(len(pol)-1):
        if pol[i:i+2] in ins:
            newpol+=ins[pol[i:i+2]]
            newpol+=pol[i+1]
    pol=newpol

counts={}
for l in set(list(pol)):
    counts[l]=pol.count(l)
answer1=max(counts.values())-min(counts.values())

pol=start
pairs=defaultdict(int)
for i in range(len(pol)-1):
    pairs[pol[i:i+2]]+=1

for s in range(40):
    ps = [p for p in pairs]
    newpairs=defaultdict(int)
    for p in ps:
        if pairs[p]<=0: continue
        for i in inpairs[p]:
            newpairs[i]+=pairs[p]
    pairs=newpairs

counts=defaultdict(int)
for p in pairs:
    counts[p[0]]+=pairs[p]
    counts[p[1]]+=pairs[p]
counts[start[0]]+=1
counts[start[-1]]+=1
counts={i:int(v/2) for i,v in counts.items()}
answer2=max(counts.values())-min(counts.values())

print(answer1,answer2)
