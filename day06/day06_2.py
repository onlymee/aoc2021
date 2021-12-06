from collections import defaultdict
with open("day06/input.txt",'r') as input:
    lines=input.read().splitlines()
answer1=-1
answer2=-1

fish=defaultdict(int)
for i in lines[0].split(','):
    fish[int(i)]+=1

def goFish(fish):
    zeros=fish[0]
    for j in range(8):
        fish[j]=fish[j+1]
    fish[6]+=zeros
    fish[8]=zeros
    
i=0
while i<80:
    goFish(fish)
    i+=1
answer1=sum(fish.values())

while i<256:
    goFish(fish)
    i+=1

answer2=sum(fish.values())

print(answer1,answer2)