answer1=-1
answer2=-1

with open("day25/input.txt",'r') as input:
    lines=input.read().splitlines()

rights=set()
downs=set()
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        if ch=='>': rights.add((r,c))
        if ch=='v': downs.add((r,c))
    
h=len(lines)
w=len(lines[0])

def steprd(rights,downs,h,w):
    delr=set()
    addr=set()
    deld=set()
    addd=set()
    for (r,c) in rights:
        dest=(r,(c+1)%w)
        if dest not in rights and dest not in downs:
            delr.add((r,c))
            addr.add(dest)
    rights=rights.difference(delr).union(addr)

    for (r,c) in downs:
        dest=((r+1)%h,c)
        if dest not in rights and dest not in downs:
            deld.add((r,c))
            addd.add(dest)

    downs=downs.difference(deld).union(addd)
    if addr or addd:
        moved=True
    else:
        moved=False
    return moved,rights,downs

            
def printMapRD(rights,downs,h,w):
    s=''
    for r in range(h):
        for c in range(w):
            if (r,c) in rights:
                s+='>'
            elif (r,c) in downs:
                s+='v'
            else:
                s+='.'
        s+='\n'
    print(s)
            
moved=True
i=0
while moved:
    i+=1
    moved=False
    moved,rights,downs = steprd(rights,downs,h,w)

answer1=i

print(answer1,answer2)
