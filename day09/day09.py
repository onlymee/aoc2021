from collections import deque
import numpy as np
answer1=-1
answer2=-1

with open("day09/input.txt",'r') as input:
    lines=input.read().splitlines()


mp={}
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        mp[(r,c)]=int(ch)

def getAdj(pnt):
    r,c=pnt
    return set([(r+1,c),(r-1,c),(r,c+1),(r,c-1)])

risk=0
lowPoints=[]
for pnt in mp:
    n=getAdj(pnt).intersection(mp)
    h=mp[pnt]
    isLow=[h<mp[np] for np in n]
    if all(isLow):
        risk+=h+1
        lowPoints.append(pnt)
answer1=risk

basins=[]
for pnt in lowPoints:
    neigh=getAdj(pnt).intersection(mp)
    queue=deque([n for n in neigh if mp[n]>=mp[pnt]])
    basin=[pnt]
    visited=set([pnt])
    while queue:
        test=queue.popleft()
        if test in visited: continue
        visited.add(test)
        if mp[test]==9: continue
        basin.append(test)
        neigh=getAdj(test).intersection(mp)
        queue.extend([n for n in neigh if mp[n]>=mp[test]])
    basins.append(basin)    

lbasins=sorted([len(b) for b in basins])
answer2=np.prod(lbasins[-3:])
print(answer1,answer2)
