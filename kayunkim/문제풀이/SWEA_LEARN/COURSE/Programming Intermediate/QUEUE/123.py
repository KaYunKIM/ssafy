def node (start,end):
    visited = [0]*(V+1)
    cnt = 2
    queue=[(start,cnt)]
    while queue:
        i,j = queue.pop(0)
        if i == end:
            return j
        else:
            for k in range(V+1):
                if graph[i][k] == 1:
                    queue.append((i,j+1))
                    print(queue)
                    graph[i][k] = j+1
                    graph[k][i] = j+1
                    # visited[ans] = 1
                    # print(visited)
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
    print(node(S,G))
    for i in graph:
        print(i)
    print()