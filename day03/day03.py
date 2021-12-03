with open("day03/input.txt",'r') as input:
    lines=input.read().splitlines()

def intFromList(x):
    return int(''.join(x),2)

digits=list(map(lambda x: ''.join(x),zip(*lines)))
gamma = intFromList(map(lambda d: '1' if d.count('1')>=len(d)/2 else '0',digits))
epsilon = intFromList(map(lambda d: '0' if d.count('1')>=len(d)/2 else '1',digits))
answer1=gamma*epsilon

def getO2(lines,digit=0):
    if len(lines)==1: 
        return int(lines[0],2)
    
    ones  = [line for line in lines if line[digit]=='1']
    zeros = [line for line in lines if line[digit]=='0']

    if len(ones)>=len(zeros):
        return getO2(ones,digit+1)
    else:
        return getO2(zeros,digit+1)

def getCO2(lines,digit=0):
    if len(lines)==1: 
        return int(lines[0],2)
    
    ones  = [line for line in lines if line[digit]=='1']
    zeros = [line for line in lines if line[digit]=='0']

    if len(ones)>=len(zeros):
        return getCO2(zeros,digit+1)
    else:
        return getCO2(ones,digit+1)

o2 =getO2 (lines)
co2=getCO2(lines)
answer2=o2*co2

print(answer1,answer2)
