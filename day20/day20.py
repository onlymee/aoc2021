from collections import defaultdict
answer1=-1
answer2=-1

with open("day20/input.txt",'r') as input:
    lines=input.read().splitlines()

algo=lines[0]

def patchValue(pnt,image,minr,maxr,minc,maxc):
    r0,c0=pnt
    digits=''
    for r in range(r0-1,r0+2):
        for c in range(c0-1,c0+2):
            if r>maxr or r<minr or c<minc or c>maxc:
                if image[(minr,minc)]=='#':
                    digits+='1'
                else:
                    digits+='0'
            elif (r,c) in image and image[(r,c)]=='#':
                 digits+='1'
            else:
                digits+='0'
    return int(digits,2)       

image={}
for r, row in enumerate(lines[2:]):
    for c,ch in enumerate(row):
        if ch=='#': image[(r,c)]=ch

def addBorder(image,inf='.'):
    rs=[r for r,_ in image]
    cs=[c for _,c in image]
    minr,maxr=min(rs),max(rs)
    minc,maxc=min(cs),max(cs)
    
    for r in range(minr-1,maxr+2):
        image[(r,minc-1)]=inf
        image[(r,maxc+1)]=inf
    for c in range(minc-1,maxc+2):
        image[(minr-1,c)]=inf
        image[(maxr+1,c)]=inf

    return image
    
def removeBorder(image):
    rs=[r for r,_ in image]
    cs=[c for _,c in image]
    minr,maxr=min(rs),max(rs)
    minc,maxc=min(cs),max(cs)
    
    for r in range(minr,maxr+1):
        del image[(r,minc)]
        del image[(r,maxc)]
    for c in range(minc+1,maxc):
        del image[(minr,c)]
        del image[(maxr,c)]

    return image

def enhance(image,algo):
    image2={}
    rs=[r for r,_ in image]
    cs=[c for _,c in image]
    minr,maxr=min(rs),max(rs)
    minc,maxc=min(cs),max(cs)
    
    for r in range(minr,maxr+1):
        for c in range(minc,maxc+1):
            idx=patchValue((r,c),image,minr,maxr,minc,maxc)
            if algo[idx]=='#':
                image2[(r,c)]=algo[idx]
    if image[(minr,minc)]=='#':
        inf=algo[511]
    else:
        inf=algo[0]
    return addBorder(image2,inf)

def disp(image,limr=None,limc=None):
    rs=[r for r,_ in image]
    cs=[c for _,c in image]
    minr,maxr=min(rs),max(rs)
    minc,maxc=min(cs),max(cs)
    s=''

    if limr: maxr=min(limr,maxr)
    if limc: maxc=min(limc,maxc)
    for r in range(minr,maxr+1):
        for c in range(minc,maxc+1):
            if (r,c) in image:
                s+=image[(r,c)]
            else:
                s+='.'
        s+='\n'
    print(s)

addBorder(image,'.')
for _ in range(2):
    image=enhance(image,algo)
removeBorder(image)
disp(image,20,20)
answer1=list(image.values()).count('#')


addBorder(image,'.')
for _ in range(48):
    image=enhance(image,algo)
removeBorder(image)
answer2=list(image.values()).count('#')

print(answer1,answer2)
