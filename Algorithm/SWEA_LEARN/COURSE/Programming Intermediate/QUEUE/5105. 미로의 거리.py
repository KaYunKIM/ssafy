di = [0,-1,0,1]
dj = [-1,0,1,0]

def bfs(i,j):
    visited = [[-1]*N for _ in range(N)]
    queue = [(i,j)]
    cnt = 0

    while queue:
        i,j = queue.pop(0)

        if miro[i][j]==3:
            return visited[i][j]

        for d in range(4):
            newi = i+di[d]
            newj = j+dj[d]

            if 0<=newi<N and 0<=newj<N and (miro[newi][newj]==0 or miro[newi][newj]==3) and visited[newi][newj]==-1:
                visited[newi][newj] = visited[i][j]+1
                queue.append((newi,newj))
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                print('#{} {}'.format(tc,bfs(i,j)))