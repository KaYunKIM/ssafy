def graph(V,start,end):
    visited = []
    stack = [start]
    while stack:
        cur = stack.pop()
        for i in mtx:
            if mtx[i][0] == cur:
                for j in mtx:
                    if mtx[i][1] == mtx[j][0]:
                        visited.append(cur)
        if cur == end:
            return 1
        elif cur != end:
            for i in mtx:
                if mtx[i][0] == cur:
                    stack.append(mtx[i][1])
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = list(map(int,input().split()))
    mtx = [list(map(int,input().split())) for _ in range(V)]
    print('#{} {}'.format(tc,graph(V,S,G)))