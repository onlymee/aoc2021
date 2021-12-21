from collections import defaultdict

# User position labels 0-9 rather than 1-10 and add extra 1 to score each time

def practice(p1,p2):
    rolls=0
    dice=1
    s1,s2=0,0
    while s1<1000 and s2<1000:    
        rolls+=3
        move=3*dice+3
        if dice==99: move=200
        if dice==100: move=103
        p1=(p1+move) % 10
        s1+=p1+1
        dice=(dice+2)%100 + 1 
        if s1>=1000: break

        rolls+=3
        move=3*dice+3
        if dice==99: move=200
        if dice==100: move=103
        p2=(p2+move) % 10
        s2+=p2+1
        dice=(dice+2)%100 + 1 
        
    return s1,s2,rolls

s1,s2,rolls=practice(10-1,6-1)
answer1=min(s1,s2)*rolls    

threeDice={}
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            s=i+j+k
            if s not in threeDice: threeDice[s]=1
            else: threeDice[s]+=1

wins={}
def getWins(state,wins={}):
    p1,p2,s1,s2=state
    if state in wins: return wins[state]

    p1wins=0
    p2wins=0
    p1nowins=defaultdict(int)
    for roll,m in threeDice.items():
        np1=(p1+roll)%10
        ns1=s1+(np1+1)
        if ns1>=21:
            p1wins+=m
        else:
            p1nowins[(np1,ns1)]+=m

    for (np1,ns1),m in p1nowins.items():
        wp2,wp1=getWins((p2,np1,s2,ns1),wins)
        p1wins+=wp1*m
        p2wins+=wp2*m
    wins[(p1,p2,s1,s2)]=(p1wins,p2wins)
    return (p1wins,p2wins)


#print(getWins((4-1,8-1,0,0)))
answer2=max(getWins((10-1,6-1,0,0)))

print(answer1,answer2)
