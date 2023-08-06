T = 10
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(input()) for _ in range(8)]
    mtx += [[mtx[x][y] for x in range(8)] for y in range(8)]
    cnt = 0
    for i in range(16):
        for j in range(0,8-N+1):
            if j == 0:
                if mtx[i][j:j+N] == mtx[i][j+N-1::-1]:
                    cnt+=1
            else:
                if mtx[i][j:j+N] == mtx[i][j+N-1:j-1:-1]:
                    cnt+=1
    print('#{} {}'.format(tc,cnt))




