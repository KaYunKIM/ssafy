def graph(V,start,end):
    visited = [0]*(V+1)
    stack = [start]

    while stack:
        cur = stack.pop()
        visited[cur] = 1
        if cur == end:
            return 1
        for t in bin[cur]:
            if visited[t] == 0:
                stack.append(t)
                V = t
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = list(map(int,input().split()))
    bin = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = list(map(int,input().split()))
        bin[a].append(b)
    S,G = list(map(int,input().split()))
    print('#{} {}'.format(tc,graph(V,S,G)))