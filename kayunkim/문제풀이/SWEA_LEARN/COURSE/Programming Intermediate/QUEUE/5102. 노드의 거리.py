def node (start,end):
    visited = [0]*(V+1)
    queue=[(start,1)]
    while queue:
        i,cnt = queue.pop(0)
        if i == end:
            return cnt-1
        else:
            for k in range(V+1):
                if graph[i][k] == 1:
                    queue.append((k,cnt+1))
                    graph[i][k] = cnt+1
                    graph[k][i] = cnt+1
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a,b = map(int,input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    S,G = map(int,input().split())
    print('#{} {}'.format(tc,node(S,G)))