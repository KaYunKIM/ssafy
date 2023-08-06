def find(x):
    if x == Parent[x]:
        return x
    else:
        return find(Parent[x])

def Union(x,y):
    Parent[find(y)] = find(x)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Parent = [0]*(N+1)

    for i in range(1, N+1):
        Parent[i] = i

    origin = list(map(int, input().split()))
    for i in range(M):
        start = origin[2*i]
        end = origin[2*i+1]
        Union(start, end)

    result = []
    for i in range(len(Parent)):
        result.append(find(i))

    print('#{} {}'.format(tc, len(set(result))-1))




# T = int(input())
#
# def rep(n):     #find_set
#     while p[n] != n:
#         n = p[n]
#     return n
#
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     l = list(map(int,input().split()))
#     p = [i for i in range(N+1)]     #make_set
#
#     for i in range(M):
#         a = l[2*i]
#         b = l[2*i+1]
#         p[rep(b)] = rep(a)   #union    #b집합의 대표를 a의 대표로 교체
#     cnt = 0
#     for i in range(1,N+1):  #대표자의 수 찾기
#         if p[i] == i:
#             cnt += 1
#     print('#{} {}'.format(tc, cnt))