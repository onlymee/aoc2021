from collections import deque,defaultdict
input=open("day02/input.txt",'r')
lines=input.read().splitlines()
input.close()

instructions=[]
for line in lines:
    bits=line.split(' ')
    instructions.append((bits[0],int(bits[1])))

x,depth=0,0
for (i,d) in instructions:
    if i=='forward': x+=d
    if i=='up':depth-=d
    if i=='down':depth+=d
answer1=x*depth

x,depth,aim=0,0,0
for (i,d) in instructions:
    if i=='forward': 
        x+=d
        depth+=aim*d
    if i=='up':aim-=d
    if i=='down':aim+=d
answer2=x*depth

print(answer1,answer2)
