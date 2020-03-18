def graph(start,end):
    visited = []
    stack = [start]

    while stack:
        if start not in visited:
            visited.append(start)
            a = stack.pop()
            stack.pop()
            for i in range(E):
                if i[0] == a:
                    graph(i[1],end)
                    stack.append(i[1])

    if visited[-1] == end:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    V,E = list(map(int,input().split()))
    lst = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        start, end = list(map(int,input().split()))
    S,G = list(map(int,input().split()))
    print(graph(S,G))