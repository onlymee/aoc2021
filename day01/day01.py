from collections import deque,defaultdict
input=open("day01/input.txt",'r')
lines=input.read().splitlines()
input.close()

ns=[int(l) for l in lines]

answer1=sum([(b-a)>0 for (a,b) in zip(ns,ns[1:])])
answer2=sum([(sum(x[1:])-sum(x[0:3]))>0 for x in zip(ns[:-3],ns[1:-2],ns[2:-1],ns[3:])])

print(answer1,answer2)
