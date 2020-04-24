di = [-1,-1,-1,0,1,1,1,0]
dj = [-1,0,1,1,1,0,-1,-1]

T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    visited = [[0]*(N+1) for _ in range(N+1)]
    visited[N//2][N//2], visited[N//2+1][N//2], visited[N//2][N//2+1], visited[N//2+1][N//2+1]= 2,1,1,2
    # board = [list(map(int, input().split())) for _ in range(M)]
    for q in range(M):
        i,j,s = list(map(int,input().split()))
        visited[i][j]=s
        for d in range(8):
            newi = i + di[d]
            newj = j + dj[d]
            bin = []
            while 0<=newi<(N+1) and 0<=newj<(N+1):
                if visited[newi][newj] !=0 and visited[newi][newj]!= s:
                    bin.append((newi, newj))
                    newi += di[d]
                    newj += dj[d]
                elif visited[newi][newj] == s:
                    if len(bin)!= 0:
                        for a in bin:
                            visited[a[0]][a[1]] = s
                    break
                elif visited[newi][newj] == 0:
                    break
    B = 0
    W = 0
    for k in visited:
        B+=k.count(1)
        W+=k.count(2)
    print('#{} {} {}'.format(tc,B,W))