from collections import defaultdict
answer1=-1
answer2=-1

with open("day12/input.txt",'r') as input:
    lines=input.read().splitlines()

mp=defaultdict(set)
for line in lines:
    fr,to = line.split('-')
    mp[fr].add(to)
    mp[to].add(fr)

def isBig(cave):
    return cave[0].lower()!=cave[0]


def search(path,mp):
    last=path[-1]
    if last=='end':
        return [path]
    hasSmall=[cave for cave in path[1:] if not isBig(cave) and path.count(cave)==2]
    if hasSmall: 
        canVisit=[]
    else: 
        canVisit=[cave for cave in path[1:] if not isBig(cave) and path.count(cave)==1]
        
    nxt=[cave for cave in mp[last] if cave!='start' and (isBig(cave) or cave not in path or cave in canVisit)]
    if not nxt: return [None]
    result=[]
    
    for cave in nxt:
        p=search(path+[cave],mp)
        result.extend([i for i in p if i])
    return result

paths=search(['start'],mp)
    
answer1=len(paths)


print(answer1,answer2)
