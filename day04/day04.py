with open("day04/input.txt",'r') as input:
    lines=input.read().splitlines()

balls=[int(i) for i in lines[0].split(',')]
balls.reverse()
lines=lines[2:]

def boardWon(board):
    for i in range(5):
        if sum(board[0+5*i:5+5*i])==-5: return True
        if sum(board[i::5])==-5: return True
    return False

def play(board,ball):
    return [-1 if x==ball else x for x in board]

# Load boards
board=[]
boardMap={}
for line in lines:
    if line=='':
        boardMap[len(boardMap)]=board
        board=[]
        continue
    ns=[line[0:2],line[3:5],line[6:8],line[9:11],line[12:15]]
    ns=[int(x.strip()) for x in ns]
    board.extend(ns)

won=[]
scores=[]
while balls:
    ball=balls.pop()
    newboards=[]
    for i,board in boardMap.items():
        if i in won: continue
        newboard=play(board,ball)
        if boardWon(newboard):
            won.append(i)
            scores.append(sum([x for x in newboard if x>0])*ball)
        boardMap[i]=newboard

print(scores[0],scores[-1])
