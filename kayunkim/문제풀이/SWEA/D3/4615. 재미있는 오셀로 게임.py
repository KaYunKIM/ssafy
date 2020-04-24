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
        for d in range(8):    #방향정하기
            newi = i + di[d]
            newj = j + dj[d]
            bin = []   #방향 바꾸고나서 초기화
            while 0<=newi<(N+1) and 0<=newj<(N+1):   #쭉 파기, 한방향!!!!!!!!!
                if visited[newi][newj] !=0 and visited[newi][newj]!= s: #반대숫자찾기
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

       0  1  2  3  4
    0 [0, 0, 0, 0, 0]
    1 [0, 2, 2, 2, 0]
    2 [0, 2, 1, 0, 0]
    3 [0, 1, 2, 0, 0]
    4 [0, 0, 0, 1, 2]