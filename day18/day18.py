answer1=-1
answer2=-1

with open("day18/input.txt",'r') as input:
    lines=input.read().splitlines()

nums=[]
for line in lines:
    nums.append(eval(line))

def leftmost(num):
    if isinstance(num,list):
        return leftmost(num[0])
    return num

def addleftmost(num,val):
    if val is None: return num
    if isinstance(num,list):
        return [addleftmost(num[0],val),num[1]]
    return num+val


def rightmost(num):
    if isinstance(num,list):
        return rightmost(num[1])
    return num

def addrightmost(num,val):
    if val is None: return num
    if isinstance(num,list):
        return [num[0],addrightmost(num[1],val)]
    return num+val

def explode(num,depth=0):
    if depth>3:
        if isinstance(num[0],int) and isinstance(num[1],int):
            return True,num[0],num[1], 0

    if isinstance(num[0],list):
        exploded, nleft, nright, res=explode(num[0],depth=depth+1)
        if exploded: 
            if nright:
                return exploded,nleft,None,[res,addleftmost(num[1],nright)]
            else:
                return exploded,nleft,None,[res,num[1]] 

    if isinstance(num[1],list):
        exploded, nleft, nright, res=explode(num[1],depth=depth+1)
        if exploded: 
            if nleft:
                return exploded,None,nright,[addrightmost(num[0],nleft),res]
            else:
                return exploded,None,nright,[num[0],res] 

    return False, None, None, num

def split(num):
    if isinstance(num,int):
        if num>=10:
            l=num // 2
            return True,[l,num-l]
    else:
        s,n0=split(num[0])    
        if s:
            return s,[n0,num[1]]
        s,n1=split(num[1])    
        if s:
            return s,[num[0],n1]
    
    return False,num
    

def reduce(num):
    change=True
    while change:
     #   print(num)
        change,_,_,num = explode(num)
        if not change: change,num = split(num)
    return num

def mag(num):
    if isinstance(num,list):
        return 3*mag(num[0])+2*mag(num[1])
    else:
        return num

total=nums[0]
for n in nums[1:]:
    total=reduce([total,n])
print(total)
answer1=mag(total)

maxmag=0
for i,m in enumerate(nums):
    for j,n in enumerate(nums):
        if i==j: continue
        maxmag=max(maxmag,mag(reduce([nums[i],nums[j]])))

answer2=maxmag

print(answer1,answer2)
