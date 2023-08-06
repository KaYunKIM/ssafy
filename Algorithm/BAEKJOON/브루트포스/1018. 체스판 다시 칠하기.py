N, M = map(int,input().split())
board = []
for _ in range(N):
    board.append(input())
x = 0
minV = 1000000000000
for x in range(0,N-8+1):
    for y in range(0,M-8+1):
        cntw = 0
        cntb=0
        for i in range(8):
            for j in range(8):
                if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                    if board[x+i][y+j]!='W':
                        cntw+=1
                    else:
                        cntb+=1
                elif (i%2==0 and j%2==1) or (i%2==1 and j%2==0):
                    if board[x+i][y+j]!='B':
                        cntw+=1
                    else:
                        cntb+=1
        cnt = min(cntw,cntb)
        if cnt < minV:
            minV = cnt
print(minV)