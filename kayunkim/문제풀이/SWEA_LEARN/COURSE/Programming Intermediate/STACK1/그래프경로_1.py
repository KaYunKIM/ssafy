def graph(n,start,end):
    visited = []
    stack = [start]

    if n == end:
        return visited
    while stack:
        cur = stack.pop()
        if cur not in visited:
            visited.append(cur)
            if cur == a:
                stack.append(b)
        graph(cur,b,end)

T = int(input())
for tc in range(1,T+1):
    V,E = list(map(int,input().split()))
    for _ in range(E):
        a,b = list(map(int,input().split()))
    S,G = list(map(input,input().split()))
    print(graph(S,0,G))