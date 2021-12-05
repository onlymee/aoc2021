from collections import defaultdict
with open("day05/input.txt",'r') as input:
    lines=input.read().splitlines()

vents=[]
for line in lines:
    bits=line.split(' -> ',2)
    x1,y1=[int(i) for i in bits[0].split(',')]
    x2,y2=[int(i) for i in bits[1].split(',')]
    if (y1,x1)>(y2,x2):
        x1,y1,x2,y2=x2,y2,x1,y1
    vents.append(((x1,y1),(x2,y2)))

def printGrid(grid):
    xs=[x for x,_ in grid]
    ys=[y for _,y in grid]
    maxx=max(xs)
    maxy=max(ys)
    minx=min(xs)
    miny=min(ys)

    for y in range(miny,maxy+1):
        l=''
        for x in range(minx,maxx+1):
            if (x,y) in grid:
                ch=str(grid[(x,y)])
            else:
                ch='.'
            l+=ch
        print(l)

grid=defaultdict(int)
for v in vents:
    (x1,y1),(x2,y2)=v
    if x1==x2:
        for y in range(y1,y2+1):
            grid[(x1,y)]+=1
    elif y1==y2:
        for x in range(x1,x2+1):
            grid[(x,y1)]+=1
    
cnt=0
for pnt in grid:
    if grid[pnt]>=2:
        cnt+=1
answer1=cnt

grid=defaultdict(int)
for v in vents:
    (x1,y1),(x2,y2)=v
    if x1==x2:
        for y in range(y1,y2+1):
            grid[(x1,y)]+=1
    elif y1==y2:
        for x in range(x1,x2+1):
            grid[(x,y1)]+=1
    else:
        if x1<x2:
            for i in range(x2-x1+1):
                grid[(x1+i,y1+i)]+=1
        else:
            for i in range(x1-x2+1):
                grid[(x1-i,y1+i)]+=1
    
cnt=0
for pnt in grid:
    if grid[pnt]>=2:
        cnt+=1
answer2=cnt

print(answer1,answer2)