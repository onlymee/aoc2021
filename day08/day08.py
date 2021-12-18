from collections import defaultdict
with open("day08/input.txt",'r') as input:
    lines=input.read().splitlines()

# Reference data
segs=['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']

counts={ch:''.join(segs).count(ch) for ch in 'abcdefg'}
sizes=[len(s) for s in segs]

# Find digit for a given segment pattern
lookup={s:str(i) for i,s in enumerate(segs)}

answer1=0
displays=[]
for line in lines:
    signal, output=line.split(' | ')
    signals=sorted([''.join(sorted(s)) for s in signal.split(' ')])
    outputs=[''.join(sorted(s)) for s in output.split(' ')]
    displays.append((signals,outputs))
    for o in outputs:
        if len(o) in [2,3,4,7]: 
            answer1+=1

def decode(ss):
    fact={}
    wires={}
    for s in ss:
        ls=len(s)
        if ls==2:
            fact[1]=set(s)
        if ls==3:
            fact[7]=set(s)
        if ls==4:
            fact[4]=set(s)
        if ls==7:
            fact[8]=set(s)
    wires['a']=fact[7].difference(fact[1]).pop()
    corf=set(fact[1]).pop()

    allwires=''.join(ss)
    if allwires.count(corf)==8:
        wires['c']=corf
        wires['f']=fact[1].difference([corf]).pop()
    else:
        wires['f']=corf
        wires['c']=fact[1].difference([corf]).pop()
    cnts={}
    for ch in 'abcdefg':
        cnt=allwires.count(ch)
        if cnt not in cnts: 
            cnts[cnt]=set([ch])
        else:
            cnts[cnt].add(ch)
    wires['e']=cnts[4].pop()
    wires['b']=cnts[6].pop()
    wires['d']=fact[4].difference(fact[1].union([wires['b']])).pop()
    wires['g']=cnts[7].difference([wires['d']]).pop()
    return {v:i for i,v in wires.items()}

answer2=0
for d in displays:
    signals,outputs=d
    wires=decode(signals)
    digits=''
    for o in outputs:
        o=sorted(''.join([wires[ch] for ch in o]))
        digits+=lookup[''.join(o)]
    val=int(digits)
    answer2+=val


print(answer1,answer2)
