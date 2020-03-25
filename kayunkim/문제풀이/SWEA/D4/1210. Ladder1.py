def ladder(row,col):
    stack = [[row,col]]

    di = [0,0,1]
    dj = [-1,1,0]

    while stack:
        nrow,ncol = stack.pop()
        if mtx[nrow][ncol] == 2:
            return col
        else:
            for d in range(3):
                newi = nrow + di[d]
                newj = ncol + dj[d]

                if 0<= newi<N and 0<= newj<N:
                    if mtx[newi][newj] == 1:
                        stack.append([newi,newj])
T = 10
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(100)]
    for i in range(100):
        if mtx[0][i] == 1:
            row, col = 0,i
            print(ladder(row,col))