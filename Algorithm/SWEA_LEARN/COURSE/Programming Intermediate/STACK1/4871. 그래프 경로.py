def graph(V,start,end):
    visited = []
    stack = [start]
    while stack:
        cur = stack.pop()
        if len(bin[cur]) != 0:
            visited.append(cur)
        if cur == end:
            visited.append(cur)
            return 1
        elif cur != end:
            for t in bin[cur]:
                if t not in stack and t not in visited:  #둘 다 없어야 중복 방지!
                    stack.append(t)
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


# def graph(V,start,end):
#     visited = []
#     stack = [start]
#     while stack:
#         cur = stack.pop()
#         for i in mtx:
#             if i[0] == cur:
#                 for j in mtx:
#                     if i[1] == j[0]:
#                         visited.append(cur)
#                         break
#         if cur == end:
#             return visited
#         elif cur != end:
#             for i in mtx:
#                 if i[0] == cur:
#                     if i[1] not in visited:
#                         stack.append(i[1])
#     return 0
#
# T = int(input())
# for tc in range(1,T+1):
#     V,E = list(map(int,input().split()))
#     mtx = [list(map(int,input().split())) for _ in range(E)]
#     S,G = list(map(int,input().split()))
#     print('#{} {}'.format(tc,graph(V,S,G)))