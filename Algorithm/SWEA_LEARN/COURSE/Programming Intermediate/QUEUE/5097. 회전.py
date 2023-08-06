T = int(input())
for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    lst = list(map(int,input().split()))
    h = 0
    while h != M:
        ans = lst.pop(0)
        lst.append(ans)
    print('#{} {}'.format(tc,lst[0])