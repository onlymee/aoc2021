with open("day06/input.txt",'r') as input:
    lines=input.read().splitlines()
answer1=-1
answer2=-1

fish = [int(i) for i in lines[0].split(',')]

i=0
while i<80:
    i+=1
    newfish=[]
    newnewfish=[]
    for f in fish:
        if f==0:
            newnewfish.append(8)
            newfish.append(6)
        else:
            f-=1
            newfish.append(f)
    fish=newfish+newnewfish

answer1=len(fish)

print(answer1,answer2)