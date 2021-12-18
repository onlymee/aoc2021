answer1=-1
answer2=-1

with open("day17/input.txt",'r') as input:
    lines=input.read().splitlines()

minx,maxx=111,161 
miny,maxy=-154,-101

#minx,maxx=20,30 
#miny,maxy=-10,-5

x,y=0,0
vx,vy=17,-4

found=False
def test(vx,vy):
    x,y=0,0
    top=0
    for _ in range(maxx*2):
#        print(x,y,vx,vy)
        x+=vx
        y+=vy
        top=max(top,y)
        if vx>0: vx=vx-1
        elif vx<0: vx=vx+1
        vy-=1
        if y<miny or x>maxx:
            break
        if x>=minx and x<=maxx and y>=miny and y<=maxy: 
            return top,True
    return 0,False

maxtop=0
good=[]
print(test(6,9))
for sx in range(1,5*maxx+2):
    for sy in range(miny,-miny):
        top,fnd=test(sx,sy)
        maxtop=max(top,maxtop)
        if fnd: good.append((sx,sy))
print(sorted(good))
answer1=maxtop
answer2=len(good)
print(answer1,answer2)
