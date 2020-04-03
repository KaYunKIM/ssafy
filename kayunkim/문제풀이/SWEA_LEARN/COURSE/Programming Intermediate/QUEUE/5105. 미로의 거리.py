di = [0,-1,0,1]
dj = [-1,0,1,0]

def bfs(i,j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    queue = [(i,j)]
    cnt = 1
    
    while queue:
        cnt += 1
        i,j = queue.pop(0)

        for d in range(4):
            newi = i + di[d]
            newj = j + dj[d]

            if 0 <= newi < N and 0 <= newj < N and (miro[newi][newj] == 0 or miro[newi][newj] == 3)   and visited[newi][newj]==0:
                queue.append((newi,newj))
                visited[newi][newj] = visited[i][j] +1
                if miro[newi][newj] == 3:
                    return visited[i][j] - 1
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    ans = 0
    for i in range(N-1,-1,-1):
        for j in range(N):
            if miro[i][j] == 2:
                print('#{} {}'.format(tc,bfs(i,j)))