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