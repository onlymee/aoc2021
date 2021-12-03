from collections import deque,defaultdict
import numpy as np

input=open("day03/input.txt",'r')
lines=input.read().splitlines()
input.close()

ns=[int(line,2) for line in lines]

nrow=len(lines)
ncol=len(lines[1])
vec=np.zeros(ncol)

for line in lines:
    vec+=np.array([int(ch) for ch in line])

gamma = np.greater(np.divide(vec,nrow*1.0),0.5)
epsilon = np.invert(gamma)

gamma=int(''.join(['1' if x else '0' for x in list(gamma)]),2)
epsilon=int(''.join(['1' if x else '0' for x in list(epsilon)]),2)

answer1=gamma*epsilon

def vecToBin(vec):
    return ''.join(['1' if x else '0' for x in vec])
def vecToInt(vec):
    return int(''.join(['1' if x else '0' for x in vec]),2)

vecs=[]
for line in lines:
    vecs.append(np.array([ch=='1' for ch in line]))


def findO2(vecs,digit):
    if len(vecs)==1: 
        return vecToInt(vecs[0])
    cnt=0
    nrow=len(vecs)
    vones=[]
    vzeros=[]
    for v in vecs:
        if v[digit]: 
            cnt+=1
            vones.append(v)
        else:
            vzeros.append(v)
    if cnt>=nrow/2:
        return findO2(vones,digit+1)
    else:
        return findO2(vzeros,digit+1)


def findCO2(vecs,digit):
    if len(vecs)==1: 
        return vecToInt(vecs[0])
    cnt=0
    nrow=len(vecs)
    vones=[]
    vzeros=[]
    for v in vecs:
        if v[digit]: 
            cnt+=1
            vones.append(v)
        else:
            vzeros.append(v)
    if cnt>=nrow/2:
        return findCO2(vzeros,digit+1)
    else:
        return findCO2(vones,digit+1)

o2=findO2(vecs,0)
co2=findCO2(vecs,0)

answer2=o2*co2

print(answer1,answer2)
