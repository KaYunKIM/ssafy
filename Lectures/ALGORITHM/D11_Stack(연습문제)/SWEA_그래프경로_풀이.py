def dfs(n,end):
    visited = [0]*(V+1)        #방문배열
    stack = []                 #스택
    stack.append(n)            #시작점 스택에, 방문했다고 표시
    visited(n) = 1

    while stack:
        n = stack.pop(0)
        if n == end:
            return 1
        for i in range(1,V+1):
            if adj[n][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        u,v = map(int,input().split())
        adj[u][v] = 1       #방향 그래프이므로 하나만
    for row in adj:
        print(row)
    S,G = map(int,input().split())
    result = dfs(S,G)
    print('#{} {}'.format(tc,result))
