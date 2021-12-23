from heapq import *
from collections import deque

def readState(file):    
    with open(file,'r') as input:
        lines=input.read().splitlines()

    mp=set()
    amphi={}
    for r,row in enumerate(lines):
        for c,ch in enumerate(row):
            if ch in "ABCD.":
                mp.add((r,c))
            if ch in "ABCD":
                idx=ord(ch)-ord('A')
                if idx in amphi:
                    amphi[idx].append((r,c))
                else:
                    amphi[idx]=[(r,c)]

    state=[]
    for a in sorted(amphi.keys()):
        if a in amphi:
            state.append(tuple(sorted(amphi[a],reverse=True)))
    return mp,fixState(tuple(state))

def fixState(state):
    res=[]
    for i,grp in enumerate(state):
        res.append(tuple(sorted(list(state[i]), reverse=True)))
    return tuple(res)

def findAllDest(mp,st):
    q=deque([(0,st)])
    localmp=set(mp)
    localmp.add(st)
    res={}
    while q:
        d,p=q.popleft()
        if p not in localmp: continue
        localmp.remove(p)
        r,c=p
        if p!=st: res[p]=d
        q.extend([(d+1,(r+1,c)),(d+1,(r-1,c)),(d+1,(r,c-1)),(d+1,(r,c+1))])
    return res

def upTuple(tpl, i, val):
    return tpl[:i] + (val,) + tpl[i + 1:]

def nextStates(state):
    res=set()
    amphis=[pos for grp in state for pos in grp]
    avail=mp.difference(amphis)
    for i,grp in enumerate(state):
        tc=i*2+3
        tr=[r for r in range(len(grp)+1,1,-1) if (r,tc) not in grp]
        if tr:
            tr=tr[0]
            for j,pos in enumerate(grp): 
                r,c=pos
                if c==tc and r>tr: continue
                cost=10**i

                dest=findAllDest(avail,state[i][j])
                if (tr,tc) in dest:
                    newstate=upTuple(state,i,upTuple(grp,j,(tr,tc)))
                    res.add((dest[(tr,tc)]*cost,fixState(newstate)))
                else:
                    for npos,d in dest.items():
                        nr,nc=npos
                        if pos[0]==1 and nr==1: continue
                        if nc in [3,5,7,9]: continue
                        newstate=upTuple(state,i,upTuple(grp,j,npos))
                        res.add((d*cost,fixState(newstate)))
    return res

def dijkstra(f, t):
    g={}
    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            if v1 not in g:
                g[v1]=nextStates(v1)
            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

def printState(state):
    map={}
    for i,grp in enumerate(state):
        for j,pos in enumerate(grp):
            map[pos]=chr(i+ord('A'))

    for p in mp:
        if p not in map: map[p]='.'
        
    s=''
    for r in range(7):
        for c in range(13):
            if (r,c) in map:
                s+=map[(r,c)]
            else:
                s+='#'
        s+='\n'
    print(s)


mp,state=readState("day23/input.txt")
_,endstate=readState("day23/target.txt")

answer1,_=dijkstra(state,endstate)

mp,state=readState("day23/input_2.txt")
_,endstate=readState("day23/target_2.txt")

answer2,_=dijkstra(state,endstate)

print(answer1,answer2)
