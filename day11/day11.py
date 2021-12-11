answer1=-1
answer2=-1

with open("day11/input.txt",'r') as input:
    lines=input.read().splitlines()

octo={}
h,w=len(lines),len(lines[0])
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        octo[(r,c)]=int(ch)

def getAdj(pnt):
    r,c=pnt
    return set([(r-1,c-1),(r,c-1),(r+1,c-1),(r-1,c),(r+1,c),(r-1,c+1),(r,c+1),(r+1,c+1)])

def printOcto(octo):
    for r in range(len(lines)):
        row=''
        for c in range(len(lines[0])):
            if octo[(r,c)]<=9:
                row+=str(octo[r,c])
            else:
                row+='X'
        print(row)
    print()


answer1=0
i=0
while True:
    flashed=set()
    #printOcto(octo)
    for o in octo:
        octo[o]+=1
    toflash=set([pnt for pnt,v in octo.items() if v>9])
    while toflash:
        flashed=flashed.union(toflash)
        toadd=[]
        for o in toflash:
           toadd.extend(getAdj(o).intersection(octo)) 
        for o in toadd:
            octo[o]+=1
        toflash=set([pnt for pnt,v in octo.items() if v>9]).difference(flashed)
    for o in flashed:
        octo[o]=0
    if i<100: answer1+=len(flashed)
    i+=1
    if len(flashed)==h*w: 
        answer2=i
        break

print(answer1,answer2)
