di = [0,1,0,-1]
dj = [1,0,-1,0]

def find(i,j):
    global maxV, cnt
    v[i][j] = 1

    for d in range(4):
        newi = i + di[d]
        newj = j + dj[d]

        if 0 <= newi < N and 0 <= newj < M and not v[newi][newj]:
            if land[newi][newj]:
                v[newi][newj] = 1
                find(newi,newj)
                v[newi][newj] = 0
                cnt += 1
            print(i, j, newi, newj, 'cnt', cnt)

    if cnt > maxV:
        maxV = cnt
    return


N, M, K = map(int,input().split())
land =[[0]*M for _ in range(N)]
v = [[0] * M for _ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())
    land[r-1][c-1] = 1

maxV = 0
for i in range(N):
    for j in range(M):
        if land[i][j]:
            cnt = 1
            find(i,j)

print(maxV)