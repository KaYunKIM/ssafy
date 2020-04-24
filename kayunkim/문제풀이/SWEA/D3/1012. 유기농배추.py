di = [-1,0,1,0]
dj = [0,1,0,-1]

def bc(i,j):
    global cnt
    queue = [(i,j)]


    while queue:
        a,b = queue.pop(0)
        visited[a][b]=1

        for d in range(4):
            newi = a + di[d]
            newj = b + dj[d]

            if 0 <=newi<N and 0<=newj<M and visited[newi][newj]==0 and land[newi][newj]==1:
                queue.append((newi,newj))
    cnt+=1
    for z in visited:
        print(z)
    print()

T = int(input())
for tc in range(1,T+1):
    M,N,K = list(map(int,input().split()))
    land = [[0]*M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    ans = 0
    for v in range(K):
        j,i = list(map(int,input().split()))
        land[i][j] = 1
        # for a in visited:
        #     print(a)
        # print()
        if visited[i][j] == 0:
            bc(i,j)
            ans+=1
    print(cnt)
    print('ans:{}'.format(ans))