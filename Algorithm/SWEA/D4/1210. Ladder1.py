def ladder(row,col):
    visited= [[0]*100 for _ in range(100)]

    di = [0, 0, -1]
    dj = [-1, 1, 0]

    while True:
        if row == 0:
            return col
        else:
            for d in range(3):
                newi = row + di[d]
                newj = col + dj[d]

                if 0<= newi<100 and 0<= newj<100:
                    if mtx[newi][newj] == 1 and visited[newi][newj]== 0:
                        row,col = newi, newj
                        visited[newi][newj] = 1
                        break
T = 10
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(100)]
    for k in range(100):
        if mtx[99][k] == 2:
            print('#{} {}'.format(tc,ladder(99,k)))
            break