def queen(i,j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    cnt = 0
    while True:
        if i == N-1:
            cnt+=1
            return
        else:
            for col in range(i+1,N):
                visited[col][j] = 1

            for dr in range(N):
                if 0<= dr<N:
                    visited[dr][dr] = 1

            for dl in range(N):
                if 0 <= dl < N:
                    visited[dl][N-dl-1] = 1

            print(visited,i)
            for newj in range(N):
                if visited[i+1][newj] == 0:
                    queen(i+1, newj)
                    
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    for k in range(N):
        print(queen(0,k))

    # print('#{} {}'.format(tc,cnt))