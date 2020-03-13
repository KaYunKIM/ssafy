def palin(N,M):
    for i in range(len(mtx)):
        for j in range(N-M+1):
            if j == 0:
                if mtx[i][j:j+M] == mtx[i][j+M-1::-1]:    #인덱싱주의!!
                    return mtx[i][j:j+M]
                break
            else:
                if mtx[i][j:j+M] == mtx[i][j+M-1:j-1:-1]:
                    return mtx[i][j:j+M]
                break
T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    mtx = [list(input()) for _ in range(N)]
    mtx+= [[mtx[x][y] for x in range(N)] for y in range(N)]
    print('#{} {}'.format(tc,''.join(palin(N,M))))