def bfs(start,end):
    visited = [0]*(V+1)
    queue = [start]
    cnt = 1
    while queue:
        queue1 = []
        while queue:
            cur = queue.pop(0)
            if visited[cur] == 0:
                visited[cur] = 1
            for i in graph[cur]:
                if i == end:
                    return cnt
                if visited[i] ==0:
                    queue1.append(i)
        queue = queue1
        cnt+=1
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    bin = [[] for _ in range(V+1)]
    for _ in range(E):
        n1,n2 = map(int,input().split())
        bin[n1].append(n2)
        bin[n2].append(n1)
    S,G = map(int,input().split())
    graph = {}
    for i in range(len(bin)):
        graph[i] = bin[i]
    print('#{} {}'.format(tc,bfs(S,G)))