answer1=-1
answer2=-1

with open("day13/input.txt",'r') as input:
    lines=input.read()

dotlines,foldlines=lines.split('\n\n')

dots=set()
for line in dotlines.split('\n'):
    c,r = line.split(',')
    dots.add((int(r),int(c)))

folds=[]
for line in foldlines.split('\n'):
    if line=='': continue
    dir,pos = line.split('=')
    folds.append((dir[-1],int(pos)))

def fold(instr,dots):
    dir,pos=instr
    if dir=='x':
        leave=[(r,c) for (r,c) in dots if c<=pos]
        mv=[(r,pos+pos-c) for (r,c) in dots if c>pos]
        return set(leave+mv)
    elif dir=='y':
        leave=[(r,c) for (r,c) in dots if r<=pos]
        mv=[(pos+pos-r,c) for (r,c) in dots if r>pos]
        return set(leave+mv)
    return dots

answer1=len(fold(folds[0],dots))

for f in folds:
    dots=fold(f,dots)


minr=min([r for r,_ in dots])
minc=min([c for _,c in dots])
maxr=max([r for r,_ in dots])
maxc=max([c for _,c in dots])
out=''
for r in range(minr,maxr+1):
    for c in range(minc,maxc+1):
        if (r,c) in dots:
            out+='#'
        else:
            out+=' '
    out+='\n'

with open("day13/output.txt",'w') as fh:
    fh.write(out)



print(answer1)

print(out)