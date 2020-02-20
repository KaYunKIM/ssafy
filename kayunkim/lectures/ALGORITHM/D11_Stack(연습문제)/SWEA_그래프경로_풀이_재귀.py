def dfs(n):
    if n == end:
        return 1
    else:
        for t in adj[n]:
            if visited == 0:
                visited[t] =1       방문표시
                if dfs(t) == 1:
    visited = {i:0 for i in range(V+1)}        #방문배열
    stack = []
    stack.append(start)
    while len(stack) != 0:
        n = stack.pop(0)
        if n == end:
            return 1
        for t in adj[n]:
            if visited[t] == 0:
                stack.append(i)
                n = t
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    visited= {i:0 for i in range(V+1)}     #방문표시
    adj = {i:[] for i in range(1,V+1)}     #{정점:[인접정점들], 정점2:[인접정점들]}
    for i in range(E):
        u,v = map(int,input().split())
        adj[u].append(v)
    start,end = map(int,input().split())
    print('#{} {}'.format(tc,dfs()))