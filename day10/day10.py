answer1=-1
answer2=-1

with open("day10/input.txt",'r') as input:
    lines=input.read().splitlines()

error={')': 3, ']': 57, '}': 1197, '>': 25137}

def syntax(msg):
    level='0'
    for ch in msg:
        if ch in '(':
            level+=')'
        elif ch in '[':
            level+=']'
        elif ch in '{':
            level+='}'
        elif ch in '<':
            level+='>'
        elif ch==level[-1]:
            level=level[:-1]
            continue
        else:
            return 0,error[ch]
    
    level=level[1:]
    score=0
    level=level[::-1]
    for ch in level:
        score=score*5+'0)]}>'.index(ch)
    print(msg,level,score)
    return score,0

incomplete=[]
answer1=0
for line in lines:
    good,bad=syntax(line)
    answer1+=bad
    if good!=0: incomplete.append(good)
incomplete.sort()
answer2=incomplete[int(len(incomplete)/2)]

print(answer1,answer2)
