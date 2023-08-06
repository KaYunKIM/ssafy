T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(N)]
    minV = 9*N
    sum = 0
    bin = []
    for i in range(N):
        for j in range(N):
            sum+= mtx[i][j]
            bin.append(j)



