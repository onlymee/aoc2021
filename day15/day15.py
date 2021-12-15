from collections import defaultdict
from heapq import *
import sys

answer1=-1
answer2=-1

with open("day15/input.txt",'r') as input:
    lines=input.read().splitlines()

mp={}
maxr=len(lines) 
maxc=len(lines[0]) 

for tr in range(5):
    for tc in range(5):
        for r,row in enumerate(lines):
            for c,ch in enumerate(row):
                d=tr+tc
                mp[(r+tr*maxr,c+tc*maxc)]=(int(ch)+d-1)%9 + 1


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

nodes = list(mp.keys())

edges=[]
for r in range(5*maxr):
    for c in range(5*maxc):
        if r>0: edges.append(((r-1,c),(r,c),mp[(r,c)]))
        if c>0: edges.append(((r,c-1),(r,c),mp[(r,c)]))
        if r<5*maxr-1: edges.append(((r+1,c),(r,c),mp[(r,c)]))
        if c<5*maxc-1: edges.append(((r,c+1),(r,c),mp[(r,c)]))

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
answer1=dijkstra(edges,(0,0),(maxr-1,maxc-1))[0]
answer2=dijkstra(edges,(0,0),((5*maxr)-1,(5*maxc)-1))[0]

print(answer1,answer2)