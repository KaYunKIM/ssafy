def ladder(i,j):
    visited = [[0]*10 for _ in range(10)]

    while True:
        print(i, j)
        if i == 0:
            return j
        else:
            di = [0, 0, -1]
            dj = [1,-1,0]


            for d in range(3):
                newi = i + di[d]
                newj = j + dj[d]

                if 0<= newi <10 and 0<= newj <10:
                    if visited[newi][newj] == 0 and mtx[newi][newj] == 1:
                        i,j = newi,newj
                        print('ni,nj : {} {}'.format(i,j))
                        visited[newi][newj] = 1

T = 1
for tc in range(1,T+1):
    N = int(input())
    mtx = [list(map(int,input().split())) for _ in range(10)]
    for k in range(10):
        if mtx[9][k] == 2:
            print('#{} {}'.format(tc,ladder(9,k)))
            break