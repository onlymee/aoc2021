answer1=-1
answer2=-1

with open("day16/input.txt",'r') as input:
    lines=input.read().splitlines()


message=lines[0]

def hex2bin(message):
    mes=''
    for ch in message:
        mes+=f'{int(ch,16):04b}'
    return mes

def readPacket(mes):
    if len(mes)<11:
        return 0,len(mes),[]
        res=-1000000000000
    vsum=0
    i=0
    ver=int(mes[0:3],2)
    vsum+=ver
    typ=int(mes[3:6],2)
    mes=mes[6:]
    i+=6
    if typ==4:
        last=False
        val=''
        while not last:
            flag=int(mes[0],2)
            val+=mes[1:5]
            mes=mes[5:]
            i+=5
            if flag==0: last=True
            if last: 
                val=int(val,2)
                #skip=4-i%4
                #mes=mes[skip:]
        res=val
    else:
        ltype=int(mes[0],2)
        mes=mes[1:]
        i+=1
        if ltype==0:
            bitlen=int(mes[:15],2)
            mes=mes[15:]
            i+=15
            svsum,di,nres = readPackets(mes[:bitlen])
            vsum+=svsum
            mes=mes[bitlen:]
            i+=bitlen
        elif ltype==1:
            paclen=int(mes[:11],2)
            mes=mes[11:]
            i+=11
            nres=[]
            for p in range(paclen):
                svsum,di,nnres=readPacket(mes)
                nres.append(nnres)
                vsum+=svsum
                mes=mes[di:]
                i+=di
        if typ==0: #sum
            res=sum(nres)
        elif typ==1: #product
            res=1
            for r in nres:
                res*=r
        elif typ==2: #min
            res=min(nres)
        elif typ==3: #max
            res=max(nres)
        elif typ==5: #gt
            res=int(nres[0]>nres[1])
        elif typ==6: #lt
            res=int(nres[0]<nres[1])
        elif typ==7: #product
            res=int(nres[0]==nres[1])
    return vsum,i,res

def readPackets(mes):
    i=0
    inPacket=False
    vsum=0
    res=[]
    while mes:
        vs,di,nres=readPacket(mes)
        vsum+=vs
        res.append(nres)
        mes=mes[di:]
        i+=di
    return vsum,i,res
#vsum1,lmes1,res1=readPackets('00111000000000000110111101000101001010010001001000000000')
#print(vsum1,lmes1,res1)
##vsum1,lmes1,res1=readPackets('11101110000000001101010000001100100000100011000001100000')
##print(vsum1,lmes1,res1)
#vsum1,lmes1,res1=readPackets(hex2bin('8A004A801A8002F478'))
#print(vsum1)
#vsum1,lmes1,res1=readPackets(hex2bin('620080001611562C8802118E34'))
#print(vsum1)
#vsum1,lmes1,res1=readPackets(hex2bin('C0015000016115A2E0802F182340'))
#print(vsum1)
#vsum1,lmes1,res1=readPackets(hex2bin('A0016C880162017C3686B18A3D4780'))
#print(vsum1)
vsum1,lmes1,res1=readPackets(hex2bin('C200B40A82'))
print(vsum1,res1)
vsum1,lmes1,res1=readPackets(hex2bin('04005AC33890'))
print(vsum1,res1)
vsum1,lmes1,res1=readPackets(hex2bin('880086C3E88112'))
print(vsum1,res1)
vsum1,lmes1,res1=readPackets(hex2bin('CE00C43D881120'))
print(vsum1,res1)
vsum, lmes, res = readPackets(hex2bin(message)) 
answer1=vsum
answer2=res[0]
print(answer1,answer2)
