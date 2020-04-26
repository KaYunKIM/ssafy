di = [-1,0,1,0]
dj = [0,1,0,-1]

def bc(i,j):
    global cnt
    queue = [(i,j)]

    while queue:
        a,b = queue.pop(0)
        if visited[a][b]==0:           #1. queue안에 중복으로 들어있는 경우, 아직 방문안한 곳만 방문하기
            visited[a][b]=1

            for d in range(4):
                newi = a + di[d]
                newj = b + dj[d]

                if 0 <=newi<N and 0<=newj<M and visited[newi][newj]==0 and land[newi][newj]==1:
                    queue.append((newi,newj))
    cnt+=1

T = int(input())
for tc in range(1,T+1):
    M,N,K = list(map(int,input().split()))
    land = [[0]*M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for v in range(K):
        j,i = list(map(int,input().split()))
        land[i][j] = 1
    for i in range(N):
        for j in range(M):
            if land[i][j] ==1 and visited[i][j]==0:
                bc(i, j)
    print(cnt)



# def bc(i,j):
#     global cnt
#     queue = [(i,j)]
#     while queue:
#         a,b = queue.pop(0)
#         visited[a][b] = 1
#
#         for d in range(4):
#             newi = a + di[d]
#             newj = b + dj[d]
#
#             if 0 <=newi<N and 0<=newj<M and visited[newi][newj]==0 and land[newi][newj]==1:
#                 if (newi,newj) not in queue:          #2. queue안에 있으면 중복 제외
#                     queue.append((newi,newj))
#     cnt+=1